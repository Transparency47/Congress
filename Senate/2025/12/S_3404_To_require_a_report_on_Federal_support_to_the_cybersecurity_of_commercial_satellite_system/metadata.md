# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3404?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3404
- Title: Satellite Cybersecurity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3404
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-04-24T15:35:26Z
- Update date including text: 2026-04-24T15:35:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3404",
    "number": "3404",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Satellite Cybersecurity Act of 2025",
    "type": "S",
    "updateDate": "2026-04-24T15:35:26Z",
    "updateDateIncludingText": "2026-04-24T15:35:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-04-14T14:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-09T20:40:13Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3404is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3404\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Peters (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require a report on Federal support to the cybersecurity of commercial satellite systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Satellite Cybersecurity Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation and the Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce, the Committee on Space, Science, and Technology, and the Committee on Homeland Security of the House of Representatives.\n**(2) Clearinghouse**\nThe term clearinghouse means the commercial satellite system cybersecurity clearinghouse required to be developed and maintained under section 4(b)(1).\n**(3) Commercial satellite system**\nThe term commercial satellite system \u2014\n**(A)**\nmeans a system that\u2014\n**(i)**\nis owned or operated by a non-Federal entity that holds a license issued by the United States for business operations; and\n**(ii)**\nis composed of not less than 1 earth satellite; and\n**(B)**\nincludes\u2014\n**(i)**\nany ground support infrastructure for each satellite in the system; and\n**(ii)**\nany transmission link among and between any satellite in the system and any ground support infrastructure in the system.\n**(4) Critical infrastructure**\nThe term critical infrastructure has the meaning given the term in subsection (e) of the Critical Infrastructure Protection Act of 2001 ( 42 U.S.C. 5195c(e) ).\n**(5) Cybersecurity risk**\nThe term cybersecurity risk has the meaning given the term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(6) Cybersecurity threat**\nThe term cybersecurity threat has the meaning given the term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 3. Report on commercial satellite cybersecurity\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study on the actions the Federal Government has taken to support the cybersecurity of commercial satellite systems, including as part of any action to address the cybersecurity of critical infrastructure sectors.\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall report to the appropriate congressional committees on the study conducted under subsection (a), which shall include information\u2014\n**(1)**\non efforts of the Federal Government, and the effectiveness of those efforts, to\u2014\n**(A)**\naddress or improve the cybersecurity of commercial satellite systems; and\n**(B)**\nsupport related efforts with international entities or the private sector;\n**(2)**\non the resources made available to the public by Federal agencies to address cybersecurity risks and threats to commercial satellite systems, including resources made available through the clearinghouse;\n**(3)**\non the extent to which commercial satellite systems are reliant on, or relied on by, critical infrastructure;\n**(4)**\nthat includes an analysis of how commercial satellite systems and the threats to those systems are integrated into Federal and non-Federal critical infrastructure risk analyses and protection plans;\n**(5)**\non the extent to which Federal agencies are reliant on commercial satellite systems and how Federal agencies mitigate cybersecurity risks associated with those systems;\n**(6)**\non the extent to which Federal agencies are reliant on commercial satellite systems that are owned wholly or in part or controlled by foreign entities, or that have infrastructure in foreign countries, and how Federal agencies mitigate associated cybersecurity risks;\n**(7)**\non the extent to which Federal agencies coordinate or duplicate authorities and take other actions focused on the cybersecurity of commercial satellite systems; and\n**(8)**\nas determined appropriate by the Comptroller General of the United States, that includes recommendations for further Federal action to support the cybersecurity of commercial satellite systems, including recommendations on information that should be shared through the clearinghouse.\n##### (c) Consultation\nIn carrying out subsections (a) and (b), the Comptroller General of the United States shall coordinate with appropriate Federal agencies and organizations, including\u2014\n**(1)**\nthe Department of Commerce;\n**(2)**\nthe Office of the National Cyber Director;\n**(3)**\nthe Department of Homeland Security;\n**(4)**\nthe Department of Defense;\n**(5)**\nthe Department of Transportation;\n**(6)**\nthe Federal Communications Commission;\n**(7)**\nthe National Aeronautics and Space Administration;\n**(8)**\nthe National Executive Committee for Space-Based Positioning, Navigation, and Timing;\n**(9)**\nthe National Space Council;\n**(10)**\nthe Department of Justice; and\n**(11)**\nthe Committee for the Assessment of Foreign Participation in the United States Telecommunications Services Sector.\n##### (d) Briefing\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall provide a briefing to the appropriate congressional committees on the study conducted under subsection (a).\n##### (e) Classification\nThe report made under subsection (b) shall be unclassified but may include a classified annex.\n#### 4. Responsibilities of the Department of Commerce\n##### (a) Small business concern defined\nIn this section, the term small business concern has the meaning given the term in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n##### (b) Establishment of commercial satellite system cybersecurity clearinghouse\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary, in coordination with the Chair of the Federal Communications Commission and the Director of the Cybersecurity and Infrastructure Security Agency, shall develop and maintain a commercial satellite system cybersecurity clearinghouse.\n**(2) Requirements**\nThe clearinghouse\u2014\n**(A)**\nshall be publicly available online;\n**(B)**\nshall contain publicly available commercial satellite system cybersecurity resources, including the voluntary recommendations consolidated under subsection (c)(1);\n**(C)**\nshall contain appropriate materials for reference by entities that develop, operate, or maintain commercial satellite systems;\n**(D)**\nshall contain materials specifically aimed at assisting small business concerns with the secure development, operation, and maintenance of commercial satellite systems; and\n**(E)**\nmay contain controlled unclassified information distributed to commercial entities through a process determined appropriate by the Secretary.\n**(3) Content maintenance**\nThe Secretary shall maintain current and relevant cybersecurity information on the clearinghouse.\n**(4) Existing platform or website**\nTo the extent practicable, the Secretary shall establish and maintain the clearinghouse using an online platform, a website, or a capability in existence as of the date of enactment of this Act.\n##### (c) Consolidation of commercial satellite system cybersecurity recommendations\n**(1) In general**\nThe Secretary, in coordination with the Secretary of Homeland Security, shall consolidate voluntary cybersecurity recommendations designed to assist in the development, maintenance, and operation of commercial satellite systems.\n**(2) Requirements**\nThe recommendations consolidated under paragraph (1) shall include materials appropriate for a public resource addressing, to the greatest extent practicable, the following:\n**(A)**\nRisk-based, cybersecurity-informed engineering, including continuous monitoring and resiliency.\n**(B)**\nPlanning for retention or recovery of positive control of commercial satellite systems in the event of a cybersecurity incident.\n**(C)**\nProtection against unauthorized access to vital commercial satellite system functions.\n**(D)**\nPhysical protection measures designed to reduce the vulnerabilities of a commercial satellite system\u2019s command, control, and telemetry receiver systems.\n**(E)**\nProtection against jamming, eavesdropping, hijacking, computer network exploitation, spoofing, threats to optical satellite communications, and electromagnetic pulse.\n**(F)**\nSecurity against threats throughout a commercial satellite system\u2019s mission lifetime.\n**(G)**\nManagement of supply chain risks that affect the cybersecurity of commercial satellite systems.\n**(H)**\nProtection against vulnerabilities posed by ownership of commercial satellite systems or commercial satellite system companies by foreign entities.\n**(I)**\nProtection against vulnerabilities posed by locating physical infrastructure, such as satellite ground control systems, in foreign countries.\n**(J)**\nAs appropriate, and as applicable pursuant to the maintenance requirement under subsection (b)(3), relevant findings and recommendations from the study conducted by the Comptroller General of the United States under section 3(a).\n**(K)**\nAny other recommendations to ensure the confidentiality, availability, and integrity of data residing on or in transit through commercial satellite systems.\n##### (d) Implementation\nIn implementing this section, the Secretary shall\u2014\n**(1)**\nto the extent practicable, carry out the implementation in partnership with the private sector;\n**(2)**\ncoordinate with\u2014\n**(A)**\nthe Secretary of Homeland Security, the Office of the National Cyber Director, the National Space Council, the Chair of the Federal Communications Commission, and the head of any other agency determined appropriate by the Office of the National Cyber Director or the National Space Council; and\n**(B)**\nthe heads of appropriate Federal agencies with expertise and experience in satellite operations, including the entities described in section 3(c) to enable the alignment of Federal efforts on commercial satellite system cybersecurity and, to the extent practicable, consistency in Federal recommendations relating to commercial satellite system cybersecurity; and\n**(3)**\nconsult with non-Federal entities developing commercial satellite systems or otherwise supporting the cybersecurity of commercial satellite systems, including private, consensus organizations that develop relevant standards.\n##### (e) Report\nNot later than 1 year after the date of enactment of this Act, and every 2 years thereafter until the date that is 9 years after the date of enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report summarizing\u2014\n**(1)**\nany partnership with the private sector described in subsection (d)(1);\n**(2)**\nany consultation with a non-Federal entity described in subsection (d)(3);\n**(3)**\nthe coordination carried out pursuant to subsection (d)(2);\n**(4)**\nthe establishment and maintenance of the clearinghouse pursuant to subsection (b);\n**(5)**\nthe recommendations consolidated pursuant to subsection (c)(1); and\n**(6)**\nany feedback received by the Secretary on the clearinghouse from non-Federal entities.\n#### 5. Strategy\nNot later than 120 days after the date of the enactment of this Act, the Secretary, jointly with the National Space Council and the Office of the National Cyber Director, in coordination with the Secretary of Homeland Security, the Director of the Office of Space Commerce, the Chair of the Federal Communications Commission, and the heads of other relevant agencies, shall submit to the appropriate congressional committees a strategy for the activities of Federal agencies to address and improve the cybersecurity of commercial satellite systems, which shall include an identification of\u2014\n**(1)**\nproposed roles and responsibilities for relevant agencies; and\n**(2)**\nas applicable, the extent to which cybersecurity threats to such systems are addressed in Federal and non-Federal critical infrastructure risk analyses and protection plans.\n#### 6. Rules of construction\nNothing in this Act shall be construed to\u2014\n**(1)**\ndesignate commercial satellite systems or other space assets as a critical infrastructure sector; or\n**(2)**\ninfringe upon or alter the authorities of the agencies described in section 3(c).",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-15T20:19:59Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2026-04-15T20:19:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-07T15:06:18Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3404is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Satellite Cybersecurity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Satellite Cybersecurity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report on Federal support to the cybersecurity of commercial satellite systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-01T04:48:17Z"
    }
  ]
}
```
