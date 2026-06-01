# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2515?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2515
- Title: American Tank Car Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2515
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-05-17T20:33:02Z
- Update date including text: 2026-05-17T20:33:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2515",
    "number": "2515",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "American Tank Car Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-17T20:33:02Z",
    "updateDateIncludingText": "2026-05-17T20:33:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-31T21:22:05Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2515ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2515\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Nehls (for himself and Mr. Moulton ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for a grant program for adoption of certain telematics systems onboard freight railcars, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Tank Car Modernization Act of 2025 .\n#### 2. Grant programs for adoption of certain telematics systems\n##### (a) Onboard freight railcar telematics systems and gateway device grant program\nThe Administrator of the Federal Railroad Administration shall establish a grant program to provide funds to freight railcar owners or operators to purchase and install\u2014\n**(1)**\nonboard freight railcar telematics systems; or\n**(2)**\nonboard freight railcar gateway devices.\n##### (b) Eligible entities\nEligible entities for funding under the grant program under this section are freight railcar owners.\n##### (c) Use of funds\nFunds provided under this section may be used to purchase and install onboard freight railcar telematic systems or onboard freight railcar gateway devices that enable the recipient of a grant to obtain and enhance the data collected from such systems and devices resulting in the following:\n**(1)**\nNear real-time visibility of freight railcar location and freight railcar asset health.\n**(2)**\nIncreasing the visibility to the safety of the asset and commodity within the freight railcar asset.\n**(3)**\nIncreasing future capability of real-time visibility in the development of onboard freight railcar sensor technology that measures or monitors, for purposes of gathering information on maintenance requirements (and enables railcar owners, operators, and shippers to identify railcars that could become a hazard)\u2014\n**(A)**\nrailcar impact;\n**(B)**\nwheel or wheel bearing temperature;\n**(C)**\nwhether a hand brake is on or off;\n**(D)**\nwhether a hatch is open or closed; and\n**(E)**\ninternal railcar temperature.\n**(4)**\nIncreasing the efficiency of railcar utilization in the North American freight railcar fleet.\n**(5)**\nReducing reliance on human and manual data capture, reducing the risk of errors due to data latency and timeliness related to freight railcar data and information.\n**(6)**\nOffering development of alerts and triggers to capture and transmit freight railcar mechanical issues to the railroad operator for action.\n**(7)**\nAbility to communicate events real-time to a wide variety of stakeholders.\n##### (d) Grant use prioritization\nIn selecting recipients of grants under this section, the Administrator shall prioritize installation of onboard freight railcar telematic systems or onboard freight railcar gateway devices in the following order of priority:\n**(1)**\nNewly built freight railcars manufactured by a qualified manufacturer in a qualified facility.\n**(2)**\nFreight railcars entering a certification event in a qualified facility.\n**(3)**\nFreight railcars entering a shopping event or maintenance event in a qualified facility.\n##### (e) Freight railcar type prioritization\nAfter establishing the priority requirements under subsection (c), the Administrator shall further ensure that the freight railcar types eligible to receive such an installation be considered in the following order of priority:\n**(1)**\nTank cars in TIH/PIH (toxic inhalation products) service.\n**(2)**\nTank cars in Class I, II, and III flammable service.\n**(3)**\nTank cars in hazardous materials service.\n**(4)**\nTank cars in specialized service.\n**(5)**\nOther tank cars.\n**(6)**\nAll other freight railcars.\n##### (f) Limitation\nTo be eligible for any expenditure of funds under this section, a freight railcar and any sensitive technology relating to such railcar shall comply with the requirements of section 20171 of title 49, United States Code.\n##### (g) Report by Secretary of Transportation\n**(1) In general**\nNot later than 3 years after the date of enactment of this Act, the Secretary of Transportation shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report on the implementation and effects of the grant program established under this section.\n**(2) Contents**\nThe report required under paragraph (1) shall include, at a minimum, the following:\n**(A)**\nThe number of railcars equipped with telematics devices using funds provided under this section.\n**(B)**\nThe cost of equipping such railcars.\n**(C)**\nThe number of safety incidents involving such railcars reported to the Federal Railroad Administration.\n**(D)**\nAnecdotal experience of grant recipients relating to the deployment of telematics devices.\n**(E)**\nAny legislative recommendations relating to the grant program established under paragraph (1).\n**(3) Public availability**\nThe report required under paragraph (1) shall be made publicly available to the maximum extent practicable without compromising confidentiality or security.\n**(4) Consultation**\nIn preparing the report required under paragraph (1), the Secretary shall consult with Federal agencies and stakeholders, as appropriate, to gather technical, operational, and safety-related data.\n##### (h) Definitions\nIn this section, the following definitions apply:\n**(1) Onboard freight railcar telematics system; onboard freight railcar gateway device**\nThe terms onboard freight railcar telematics system and onboard freight railcar gateway device mean the telematics or gateway device physically installed on a freight railcar that is owned by a railcar owner that collects and transmits data about the railcar asset.\n**(2) Telematics**\nThe term telematics means a technology that\u2014\n**(A)**\nrelies on telecommunications, informatics, and computer and data processing;\n**(B)**\ngenerates data and informatics from gateway devices fixed to railcars and provides for the exchange of information over a distance using battery or solar powered wireless connections; and\n**(C)**\nincludes the method upon which freight railcars are monitored by using GPS technology through a gateway device using on-board diagnostics to plot a railcar\u2019s movements and, if applicable, gather railcar equipment health and condition data from other onboard railcar sensors when applied.\n**(3) Gateway device**\nThe term gateway device means a network hardware or software node used in freight railcar telecommunications that\u2014\n**(A)**\nconnects two networks with different transmission protocols together;\n**(B)**\nserves as an entry and exit point for a network as all data collected from the railcar must pass through or communicate with the gateway prior to being routed;\n**(C)**\nare distinct from routers or switches in that they communicate using more than one protocol to connect multiple networks; and\n**(D)**\nmay be any device on a freight railcar that is embedded with electronics, software, sensors, or other connectivity, that enables the device to connect to, collect data from, or exchange data with another device, including\u2014\n**(i)**\nrailcar onboard telematics;\n**(ii)**\nglobal positioning system satellite and cellular location tracking systems;\n**(iii)**\nrailcar event status sensors;\n**(iv)**\nrailcar predictive component condition and performance monitoring sensors; and\n**(v)**\nsimilar technologies embedded into freight railcar components and sub-assemblies.\n**(4) Railroad freight car**\nThe term railroad freight car means a car designed to carry freight or railroad personnel by rail, including\u2014\n**(A)**\na box railcar;\n**(B)**\na refrigerator railcar;\n**(C)**\na ventilator railcar;\n**(D)**\nan intermodal well railcar;\n**(E)**\na gondola railcar;\n**(F)**\na hopper railcar;\n**(G)**\nan auto rack railcar;\n**(H)**\na flat railcar;\n**(I)**\na special railcar;\n**(J)**\na caboose railcar;\n**(K)**\na tank railcar; and\n**(L)**\na yard railcar.\n**(5) Qualified facility**\nThe term qualified facility means a facility that is not owned or under the control of a state-owned enterprise.\n**(6) Qualified manufacturer**\nThe term qualified manufacturer means a railroad freight car manufacturer that is not owned or under the control of a state-owned enterprise.\n**(7) Certification event**\nThe term certification event means a railroad freight car that is required by current regulations to be recertified in a maintenance facility or qualified facility.\n**(8) Shopping event**\nThe term shopping event means a railroad freight car that is undergoing regular or routine maintenance by a railcar maintenance facility or qualified facility.\n**(9) State-owned enterprise**\nThe term state-owned enterprise means\u2014\n**(A)**\nan entity that is owned by, or under the control of, a national, provincial, or local government of a country of concern, or an agency of such government; or\n**(B)**\nan individual acting under the direction or influence of a government or agency described in subparagraph (A).\n**(10) Country of concern**\nThe term country of concern means a country that\u2014\n**(A)**\nis identified by the Department of Commerce as a nonmarket economy country (as defined in section 771(18) of the Tariff Act of 1930 ( 19 U.S.C. 1677(18) )) as of the date of enactment of the Passenger Rail Expansion and Rail Safety Act of 2021;\n**(B)**\nwas identified by the United States Trade Representative in the most recent report required by section 182 of the Trade Act of 1974 ( 19 U.S.C. 2242 ) as a foreign country included on the priority watch list (as defined in subsection (g)(3) of such section); and\n**(C)**\nis subject to monitoring by the Trade Representative under section 306 of the Trade Act of 1974 ( 19 U.S.C. 2416 ).\n##### (i) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $100,000,000 for each of fiscal years 2026 through 2029, to remain available until expended.\n#### 3. Enhancing freight railcar onboard telematics and sensor development pilot program\n##### (a) Establishment\nThe Administrator of the Federal Railroad Administration shall establish a pilot program to\u2014\n**(1)**\nassist freight railcar owners and freight railcar manufacturers in the development of freight railcar onboard sensor technologies to add visibility to the safety of the freight railcar asset and commodity within the freight railcar asset;\n**(2)**\nencourage development of freight railcar onboard sensors that communicate to the freight railcar onboard gateway devices to offer future capabilities of real-time visibility of\u2014\n**(A)**\nwheel and wheel bearing temperature;\n**(B)**\nwhether a hand brake is on or off;\n**(C)**\nwhether a hatch is open or closed; and\n**(D)**\ninternal railcar temperature; and\n**(3)**\ncarry out any of the activities described in paragraph (1) and (2) for purposes of informing railcar owners or operators on maintenance requirements, and enable operators, shippers, and railcar owners to possibly identify railcars that could become a hazard.\n##### (b) Eligible entities\nEligible entities for funding under the pilot program under this section are freight railcar owners.\n##### (c) Limitation\nTo be eligible for any expenditure of funds under this section, a freight railcar and any sensitive technology relating to such railcar shall comply with the requirements of section 20171 of title 49, United States Code.\n##### (d) Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Administrator shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report on\u2014\n**(1)**\nthe activities carried out with funds provided under this section; and\n**(2)**\nthe effectiveness of developed freight railcar onboard sensors by outlining the types and numbers of sensors that have become industry accepted and are in use on freight railcars.\n##### (e) Definitions\n**(1) Freight railcar onboard sensor**\nThe term freight railcar onboard sensor means the onboard sensor that communicates or signals the freight railcar onboard telematics device or gateway device physically installed on a freight railcar that is purchased and installed by, and owned by the railcar owner that collects and transmits data about the railcar asset to the railcar owner, data system, or data collection point.\n**(2) Railroad freight car**\nThe term railroad freight car means a car designed to carry freight or railroad personnel by rail, including\u2014\n**(A)**\na box railcar;\n**(B)**\na refrigerator railcar;\n**(C)**\na ventilator railcar;\n**(D)**\nan intermodal well railcar;\n**(E)**\na gondola railcar;\n**(F)**\na hopper railcar;\n**(G)**\nan auto rack railcar;\n**(H)**\na flat railcar;\n**(I)**\na special railcar;\n**(J)**\na caboose railcar;\n**(K)**\na tank railcar; and\n**(L)**\na yard railcar.\n**(3) Telematics**\nThe term telematics means a technology that\u2014\n**(A)**\nrelies on telecommunications, informatics, and computer and data processing;\n**(B)**\ngenerates data and informatics from gateway devices fixed to railcars and provide for the exchange of information over a distance using battery or solar powered wireless connections; and\n**(C)**\nincludes the method upon which freight railcars are monitored by using GPS technology through a gateway device using on-board diagnostics to plot a railcar\u2019s movements and, if applicable, gather railcar equipment health and condition data from other onboard railcar sensors when applied.\n**(4) Gateway device**\nThe term gateway device means a network hardware or software node used in freight railcar telecommunications that\u2014\n**(A)**\nconnects two networks with different transmission protocols together;\n**(B)**\nserve as an entry and exit point for a network as all data collected from the railcar must pass through or communicate with the gateway prior to being routed;\n**(C)**\nare distinct from routers or switches in that they communicate using more than one protocol to connect multiple networks; and\n**(D)**\nmay be any device on a freight railcar that is embedded with electronics, software, sensors, or other connectivity, that enables the device to connect to, collect data from, or exchange data with another device, including\u2014\n**(i)**\nrailcar onboard telematics;\n**(ii)**\nglobal positioning system satellite and cellular location tracking systems;\n**(iii)**\nrailcar event status sensors;\n**(iv)**\nrailcar predictive component condition and performance monitoring sensors; and\n**(v)**\nsimilar sensitive technologies embedded into freight railcar components and sub-assemblies.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2029, to remain available until expended.",
      "versionDate": "2025-03-31",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-04-08T12:43:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2515",
          "measure-number": "2515",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2026-05-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2515v00",
            "update-date": "2026-05-17"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Tank Car Modernization Act of 2025</strong></p><p>This bill establishes new Federal Railroad Administration (FRA) pilot and grant programs to outfit tank railcars with onboard sensors capable of delivering real-time safety-related condition data while a train is in motion.</p><p>Specifically, the FRA must establish a grant program for freight railcar owners or operators to purchase and install (1) onboard freight railcar\u00a0telematics systems (for wirelessly communicating a railcar's location and health), or (2) onboard freight railcar gateway devices (for collecting and exchanging data between railcar devices, including monitoring and\u00a0telematics systems).</p><p>In selecting grant recipients, the FRA must prioritize installation of these systems or devices in newly built tank railcars and by the type of load carried, starting with tank cars in TIH/PIH (toxic or poison inhalation hazard) service.</p><p>In addition, the FRA must establish a pilot program to</p><ul><li>assist freight railcar owners and manufacturers in the development of onboard sensor technologies in order to add visibility to the safety of freight railcars, and</li><li>encourage development of freight railcar onboard sensors that communicate to the freight railcar onboard gateway devices to offer future capabilities of real-time visibility (e.g., wheel and wheel bearing temperature).</li></ul>"
        },
        "title": "American Tank Car Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2515.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Tank Car Modernization Act of 2025</strong></p><p>This bill establishes new Federal Railroad Administration (FRA) pilot and grant programs to outfit tank railcars with onboard sensors capable of delivering real-time safety-related condition data while a train is in motion.</p><p>Specifically, the FRA must establish a grant program for freight railcar owners or operators to purchase and install (1) onboard freight railcar\u00a0telematics systems (for wirelessly communicating a railcar's location and health), or (2) onboard freight railcar gateway devices (for collecting and exchanging data between railcar devices, including monitoring and\u00a0telematics systems).</p><p>In selecting grant recipients, the FRA must prioritize installation of these systems or devices in newly built tank railcars and by the type of load carried, starting with tank cars in TIH/PIH (toxic or poison inhalation hazard) service.</p><p>In addition, the FRA must establish a pilot program to</p><ul><li>assist freight railcar owners and manufacturers in the development of onboard sensor technologies in order to add visibility to the safety of freight railcars, and</li><li>encourage development of freight railcar onboard sensors that communicate to the freight railcar onboard gateway devices to offer future capabilities of real-time visibility (e.g., wheel and wheel bearing temperature).</li></ul>",
      "updateDate": "2026-05-17",
      "versionCode": "id119hr2515"
    },
    "title": "American Tank Car Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Tank Car Modernization Act of 2025</strong></p><p>This bill establishes new Federal Railroad Administration (FRA) pilot and grant programs to outfit tank railcars with onboard sensors capable of delivering real-time safety-related condition data while a train is in motion.</p><p>Specifically, the FRA must establish a grant program for freight railcar owners or operators to purchase and install (1) onboard freight railcar\u00a0telematics systems (for wirelessly communicating a railcar's location and health), or (2) onboard freight railcar gateway devices (for collecting and exchanging data between railcar devices, including monitoring and\u00a0telematics systems).</p><p>In selecting grant recipients, the FRA must prioritize installation of these systems or devices in newly built tank railcars and by the type of load carried, starting with tank cars in TIH/PIH (toxic or poison inhalation hazard) service.</p><p>In addition, the FRA must establish a pilot program to</p><ul><li>assist freight railcar owners and manufacturers in the development of onboard sensor technologies in order to add visibility to the safety of freight railcars, and</li><li>encourage development of freight railcar onboard sensors that communicate to the freight railcar onboard gateway devices to offer future capabilities of real-time visibility (e.g., wheel and wheel bearing temperature).</li></ul>",
      "updateDate": "2026-05-17",
      "versionCode": "id119hr2515"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2515ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "American Tank Car Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Tank Car Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a grant program for adoption of certain telematics systems onboard freight railcars, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:30Z"
    }
  ]
}
```
