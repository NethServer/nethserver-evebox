<?php
namespace NethServer\Module\Dashboard\Applications;

/*
 * Copyright (C) 2017 Nethesis S.r.l.
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * Evebox web interface
 *
 * @author Giacomo Sanchietti
 */
class Evebox extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Evebox";
    }

    public function getInfo()
    {
        $configDb = $this->getPlatform()->getDatabase('configuration');
        $host = explode(':',$_SERVER['HTTP_HOST']);
        $alias = $configDb->getProp('evebox', 'alias');
        return array(
            'url' => "/".$alias
            );
    }
}

