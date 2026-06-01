# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4240?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4240
- Title: Countering Untrusted Telecommunications Abroad Act
- Congress: 119
- Bill type: HR
- Bill number: 4240
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-11-18T09:05:46Z
- Update date including text: 2025-11-18T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4240",
    "number": "4240",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Countering Untrusted Telecommunications Abroad Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:46Z",
    "updateDateIncludingText": "2025-11-18T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "AS"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4240ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4240\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Moskowitz (for himself and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish certain reporting and other requirements relating to telecommunications equipment and services produced or provided by certain entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Untrusted Telecommunications Abroad Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe national security of the United States is affected by the telecommunications security of United States allies, partners, and other countries around the globe;\n**(2)**\nthe importance of mobile and internet services makes such services tempting and effective tools for malign influence and economic coercion;\n**(3)**\nHuawei Technologies Company and ZTE Corporation (and any subsidiary or affiliate of either such entity) should not serve as a vendor of telecommunications equipment or services given the close ties to, and control over, such entities by the People\u2019s Republic of China; and\n**(4)**\nit is in the economic and national security interests of the United States to ensure that countries around the globe use trusted telecommunications equipment or services.\n#### 3. Report on untrusted telecommunications equipment or services in countries with collective defense agreement with United States\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for two years, the Secretary of State, in consultation with the Assistant Secretary of Commerce for Communications and Information, shall submit to the Committees on Foreign Affairs and Energy and Commerce of the House of Representatives and the Committees on Foreign Relations and Commerce, Science, and Transportation of the Senate a report on the prevalence of untrusted telecommunications equipment or services in the networks of United States allies and partners.\n##### (b) Matters\nThe report under subsection (a) shall enumerate each United States ally or partner with respect to which the United States has entered into a collective defense agreement and include, for each such country, the following:\n**(1)**\nA description of the presence, or lack thereof, of untrusted telecommunications equipment or services in any 5G network of the country.\n**(2)**\nIf any untrusted telecommunications equipment or service is present in such a network\u2014\n**(A)**\nan enumeration of any mobile carriers that are using the untrusted telecommunications equipment or service present, and any mobile carriers that are not;\n**(B)**\na determination of whether the untrusted telecommunications equipment or service present is in the core or periphery of the network; and\n**(C)**\nany plans by the United States ally or partner, or the individual mobile carrier, to rip and replace the untrusted telecommunications equipment or service present with a trusted telecommunications equipment or service.\n**(3)**\nA description of any plans by network operators to use untrusted communications equipment or services in the deployment of Open Radio Access Network (Open RAN) technology, or any successor to such technology, or in future 6G networks.\n#### 4. Report on covered telecommunications equipment or services in United States embassies\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Comptroller General of the United States has reported that 23 percent of all telecommunications device manufacturers of the Department of State have at least one supplier reported to be headquartered in the People\u2019s Republic of China or the Russian Federation.\n**(2)**\nThe Comptroller General has reported that four percent of all telecommunications contractors of the Department of State have at least one supplier reported to be headquartered in the People\u2019s Republic of China.\n##### (b) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in consultation with the heads of such other departments and agencies as the Secretary determines necessary, shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report containing an assessment of the use of covered telecommunications equipment or services in United States embassies and by United States embassy staff and personnel.\n**(2) Matters**\nThe report under paragraph (1) shall include information on the following:\n**(A)**\nThe status of the implementation by the Secretary of State of the prohibition under subsection (a)(1) of section 889 of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 132 Stat. 1917; 41 U.S.C. 3901 note prec.) with respect to equipment, systems, and services used at United States embassies, including\u2014\n**(i)**\nan identification of the United States embassies with respect to which the Secretary has implemented such prohibition, and an identification of those with respect to which the Secretary has not implemented such prohibition, if any;\n**(ii)**\nan identification of any difficulties that have delayed the implementation of such prohibition by the Secretary with respect to United States embassies, such as visibility into supply chains, costs of equipment replacement, and plans for timely remediation;\n**(iii)**\ninformation on any waivers that have been granted to an entity under subsection (d) of such section 889 for equipment, systems, or services used at United States embassies, including a justification of why each waiver was granted and any other information required pursuant to paragraph (1)(B) of such subsection; and\n**(iv)**\nfor any entity that has sought a waiver specified in clause (iii), the implementation status of the phase-out plan of the entity submitted by the entity pursuant to subsection (d) of such section 889.\n**(B)**\nInformation regarding the extent to which the digital devices of United States embassy staff and personnel are serviced by Huawei Technologies Company or ZTE Corporation (or any subsidiary or affiliate of either such entity), or any other entity headquartered in the People\u2019s Republic of China, and an assessment of the likelihood of the intelligence services of the People\u2019s Republic of China gaining access to the contents and data of the digital devices used by United States embassy personnel as a result of any such servicing.\n**(C)**\nAny other information regarding ongoing efforts to safeguard the communications security of United States embassies.\n**(3) Form**\nThe report under paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n#### 5. Supporting trusted telecommunications\n##### (a) In general\nThe Secretary of State, in consultation with the Assistant Secretary of Commerce for Communications and Information, shall select for the provision of support under this section telecommunications infrastructure projects that have the potential, as determined by the Secretary, to promote the national security of the United States and meet such other requirements as the Secretary may prescribe.\n##### (b) Diplomatic and political support\nThe Secretary of State shall provide to each project selected under subsection (a), as appropriate, diplomatic and political support, including by using the diplomatic and political influence and expertise of the Department of State to build the capacity of countries to resolve any impediments to the development of the project.\n##### (c) Early stage project support\nThe Director of the United States Trade and Development Agency should provide, as appropriate, early-stage project support with respect to projects selected under subsection (a).\n#### 6. Definitions\nIn this Act:\n**(1) Covered telecommunications equipment or service; untrusted telecommunications equipment or service**\nThe terms covered telecommunications equipment or service and untrusted telecommunications equipment or service have the meaning given to the term covered communications equipment or service in section 9 of the Secure and Trusted Communications Network Act of 2019 ( 47 U.S.C. 1608 ).\n**(2) Trusted telecommunications equipment or service**\nThe term trusted telecommunications equipment or service means any telecommunications equipment or service that is not a covered telecommunications equipment or service.",
      "versionDate": "2025-06-27",
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
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:38:19Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4240ih.xml"
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
      "title": "Countering Untrusted Telecommunications Abroad Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T05:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Untrusted Telecommunications Abroad Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish certain reporting and other requirements relating to telecommunications equipment and services produced or provided by certain entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T05:33:39Z"
    }
  ]
}
```
