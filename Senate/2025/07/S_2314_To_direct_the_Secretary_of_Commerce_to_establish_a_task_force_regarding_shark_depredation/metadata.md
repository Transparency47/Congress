# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2314
- Title: SHARKED Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2314
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-04-09T12:55:04Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-07-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2026-03-04 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.
- 2026-03-04 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.
- 2026-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 349.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-07-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2026-03-04 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.
- 2026-03-04 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.
- 2026-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 349.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2314",
    "number": "2314",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SHARKED Act of 2025",
    "type": "S",
    "updateDate": "2026-04-09T12:55:04Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 349.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-114.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
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
            "date": "2026-03-04T20:00:47Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:07:54Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-16T23:29:57Z",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "HI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2314is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2314\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Scott of Florida (for himself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025 .\n#### 2. Shark depredation task force and research projects\n##### (a) Shark depredation task force\n**(1) In general**\nThe Secretary of Commerce shall establish a task force (referred to in this subsection as the task force ) to identify and address critical needs with respect to shark depredation.\n**(2) Membership**\nThe Secretary of Commerce shall appoint individuals to the task force, including\u2014\n**(A)**\n1 representative from\u2014\n**(i)**\neach Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) );\n**(ii)**\neach Marine Fisheries Commission, as such term is defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 );\n**(iii)**\nthe fish and wildlife agency of a coastal State from each Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) ); and\n**(iv)**\nthe National Marine Fisheries Service;\n**(B)**\nan individual with expertise in the management of highly migratory species;\n**(C)**\na researcher with expertise in shark management and behavior; and\n**(D)**\na researcher with expertise in shark ecology.\n**(3) Responsibilities**\nThe task force shall\u2014\n**(A)**\ndevelop ways to improve coordination and communication across the fisheries management community and shark research community to address shark depredation;\n**(B)**\nidentify research priorities and funding opportunities for such priorities, including\u2014\n**(i)**\nidentifying shark species involved in interactions;\n**(ii)**\nshark stock assessments;\n**(iii)**\nhow sharks become habituated to humans and thus lead to more interactions between sharks and humans;\n**(iv)**\nhow angler behavior and fishery regulatory frameworks may influence shark interactions;\n**(v)**\ntechniques and strategies to reduce harmful interactions between sharks and humans, including the development and use of non-lethal deterrents;\n**(vi)**\nthe role of healthy shark populations in the ocean food web; and\n**(vii)**\nclimate change impacts on shifting shark populations, prey, and shark behavior;\n**(C)**\ndevelop recommended management strategies to address shark depredation; and\n**(D)**\ncoordinate the development and distribution of educational materials to help the fishing community minimize shark interactions, including through changed angler behavior and expectations.\n**(4) Report**\nNot later than 2 years after the date of enactment of this section, and every 2 years thereafter until the termination of the task force in accordance with paragraph (5), the task force shall submit to Congress a report regarding the findings of the task force.\n**(5) Sunset**\nThe task force shall terminate not later than 7 years after the date on which the Secretary of Commerce establishes the task force.\n**(6) Coastal state defined**\nIn this subsection, the term coastal State \u2014\n**(A)**\nmeans a State of the United States in, or bordering on, the Atlantic Ocean, Pacific Ocean, Arctic Ocean, Gulf of Mexico, or Long Island Sound; and\n**(B)**\nincludes Puerto Rico, the Virgin Islands of the United States, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.\n##### (b) Shark depredation research projects\nSection 318(c) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1867(c) ) is amended by adding at the end the following:\n(6) Projects to better understand shark depredation, including identifying what causes increases in shark depredation and determining how to best address shark depredation. .\n##### (c) Effect\nNothing in this section shall be construed to affect the authority and responsibility of the Secretary of Commerce in carrying out the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) or the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ).",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2314rs.xml",
      "text": "II\nCalendar No. 349\n119th CONGRESS\n2d Session\nS. 2314\n[Report No. 119\u2013114]\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Scott of Florida (for himself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nMarch 4, 2026 Reported by Mr. Cruz , without amendment\nA BILL\nTo direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025 .\n#### 2. Shark depredation task force and research projects\n##### (a) Shark depredation task force\n**(1) In general**\nThe Secretary of Commerce shall establish a task force (referred to in this subsection as the task force ) to identify and address critical needs with respect to shark depredation.\n**(2) Membership**\nThe Secretary of Commerce shall appoint individuals to the task force, including\u2014\n**(A)**\n1 representative from\u2014\n**(i)**\neach Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) );\n**(ii)**\neach Marine Fisheries Commission, as such term is defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 );\n**(iii)**\nthe fish and wildlife agency of a coastal State from each Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) ); and\n**(iv)**\nthe National Marine Fisheries Service;\n**(B)**\nan individual with expertise in the management of highly migratory species;\n**(C)**\na researcher with expertise in shark management and behavior; and\n**(D)**\na researcher with expertise in shark ecology.\n**(3) Responsibilities**\nThe task force shall\u2014\n**(A)**\ndevelop ways to improve coordination and communication across the fisheries management community and shark research community to address shark depredation;\n**(B)**\nidentify research priorities and funding opportunities for such priorities, including\u2014\n**(i)**\nidentifying shark species involved in interactions;\n**(ii)**\nshark stock assessments;\n**(iii)**\nhow sharks become habituated to humans and thus lead to more interactions between sharks and humans;\n**(iv)**\nhow angler behavior and fishery regulatory frameworks may influence shark interactions;\n**(v)**\ntechniques and strategies to reduce harmful interactions between sharks and humans, including the development and use of non-lethal deterrents;\n**(vi)**\nthe role of healthy shark populations in the ocean food web; and\n**(vii)**\nclimate change impacts on shifting shark populations, prey, and shark behavior;\n**(C)**\ndevelop recommended management strategies to address shark depredation; and\n**(D)**\ncoordinate the development and distribution of educational materials to help the fishing community minimize shark interactions, including through changed angler behavior and expectations.\n**(4) Report**\nNot later than 2 years after the date of enactment of this section, and every 2 years thereafter until the termination of the task force in accordance with paragraph (5), the task force shall submit to Congress a report regarding the findings of the task force.\n**(5) Sunset**\nThe task force shall terminate not later than 7 years after the date on which the Secretary of Commerce establishes the task force.\n**(6) Coastal state defined**\nIn this subsection, the term coastal State \u2014\n**(A)**\nmeans a State of the United States in, or bordering on, the Atlantic Ocean, Pacific Ocean, Arctic Ocean, Gulf of Mexico, or Long Island Sound; and\n**(B)**\nincludes Puerto Rico, the Virgin Islands of the United States, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.\n##### (b) Shark depredation research projects\nSection 318(c) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1867(c) ) is amended by adding at the end the following:\n(6) Projects to better understand shark depredation, including identifying what causes increases in shark depredation and determining how to best address shark depredation. .\n##### (c) Effect\nNothing in this section shall be construed to affect the authority and responsibility of the Secretary of Commerce in carrying out the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) or the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ).",
      "versionDate": "2026-03-04",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-22",
        "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "207",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Related bill"
          },
          {
            "identifiedBy": "CRS",
            "type": "Identical bill"
          }
        ]
      },
      "title": "SHARKED Act of 2025",
      "type": "HR"
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-27T13:18:36Z"
          },
          {
            "name": "Aquatic ecology",
            "updateDate": "2025-08-27T13:18:44Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-27T13:18:52Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-08-27T13:18:58Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2025-08-27T13:19:05Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-08-27T13:19:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-31T21:05:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s2314",
          "measure-number": "2314",
          "measure-type": "s",
          "orig-publish-date": "2025-07-16",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": [
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119s2314v25",
              "update-date": "2026-04-08"
            },
            "action-date": "2026-03-04",
            "action-desc": "Reported to Senate",
            "summary-text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>"
          },
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119s2314v00",
              "update-date": "2026-04-09"
            },
            "action-date": "2025-07-16",
            "action-desc": "Introduced in Senate",
            "summary-text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>"
          }
        ],
        "title": "SHARKED Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2314.xml",
    "summary": {
      "actionDate": "2026-03-04",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2314"
    },
    "title": "SHARKED Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2026-03-04",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2314"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2314is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2314rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SHARKED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T11:58:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "SHARKED Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-06T03:53:21Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-06T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHARKED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:34Z"
    }
  ]
}
```
