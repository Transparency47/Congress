# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2505
- Title: Block the Use of Transatlantic Technology in Iranian Made Drones Act
- Congress: 119
- Bill type: HR
- Bill number: 2505
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-09-16T08:05:41Z
- Update date including text: 2025-09-16T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 50 - 0.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 50 - 0.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2505",
    "number": "2505",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act",
    "type": "HR",
    "updateDate": "2025-09-16T08:05:41Z",
    "updateDateIncludingText": "2025-09-16T08:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 50 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
        "item": [
          {
            "date": "2025-07-22T15:22:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-31T16:05:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "SC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "IA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2505ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2505\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Keating (for himself and Mr. Wilson of South Carolina ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the development of strategies and options to prevent the export to Iran of certain technologies related to unmanned aircraft systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Block the Use of Transatlantic Technology in Iranian Made Drones Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Iranian regime has provided financial and material support, including the provision of unmanned aircraft systems, to United States adversaries, including terrorist organizations such as Hamas, Hezbollah, the Houthis, and Palestinian Islamic Jihad, and the Russian Federation as a part of its illegal war of aggression against Ukraine.\n**(2)**\nIn 2022, the United States established an interagency task force to investigate how United States and Western-made technology has been incorporated into unmanned aircraft systems produced by Iran and take appropriate steps in response.\n**(3)**\nOn June 9, 2023, the Department of State, the Department of Justice, the Department of Commerce, and the Department of the Treasury issued a joint advisory to alert persons and businesses globally to the threat of Iran\u2019s unmanned aircraft systems and the need to take appropriate steps to avoid or prevent any activities that would support the further development of Iran\u2019s unmanned aircraft program.\n**(4)**\nIn recent years the United States enacted sanctions targeting\u2014\n**(A)**\nthe unmanned aircraft industry and missile industry of Iran;\n**(B)**\nentities, individuals, and vessels that played a central role in facilitating and financing the clandestine sale of Iranian unmanned aerial vehicles; and\n**(C)**\nentities associated with the Iranian defense ministry\u2019s procurement of critical components for missiles and drones.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ncontrolling the end use of dual use technology and highly ubiquitous parts thereof in the global market is difficult for manufacturers and government regulators alike;\n**(2)**\nIranian-made unmanned aircraft systems play a key role in the Russian Federation\u2019s illegal war of aggression against Ukraine, including attacks on civilian population centers and critical infrastructure such as power plants and ports; and\n**(3)**\nthe United States, along with the allies and partners of the United States, must ensure that technology designed or produced by United States or using certain United States software, technology, or production equipment, is not used to support the Russian Federation\u2019s war of aggression against Ukraine or used by Hamas to attack Israel, particularly in the case of unmanned aircraft systems produced by Iran.\n#### 4. Strategies to prevent export to Iran of certain technologies related to unmanned aircraft systems\n##### (a) Department of commerce strategy\n**(1) Strategy required**\nThe Secretary of Commerce (in consultation with the Secretary of State, the Secretary of Defense, and the Director of National Intelligence) shall develop a strategy to prevent the illegal export to Iran by United States persons regarding technologies used or that may be used in the design, development, production, or operational employment of unmanned aircraft systems by Iran, including the following microelectronics:\n**(A)**\nMicrocontrollers.\n**(B)**\nVoltage regulators.\n**(C)**\nDigital signal controllers.\n**(D)**\nGPS modules.\n**(E)**\nMicroprocessors.\n**(2) Elements**\nThe strategy under paragraph (1) shall include, at a minimum, the following elements:\n**(A)**\nA process for the Secretary of Commerce (in coordination with the Secretaries and heads specified in paragraph (1)) to proactively identify\u2014\n**(i)**\ncurrent and emerging technologies used or that may be used by Iran in the design, development, production, or operational employment of unmanned aircraft systems (including critical components thereof);\n**(ii)**\nUnited States manufacturers of such technologies; and\n**(iii)**\nforeign manufacturers and proliferators of such technologies.\n**(B)**\nA process for the Secretary of Commerce (in coordination with the Secretaries and heads specified in paragraph (1)) to proactively identify third-party distributors and resellers of the technologies specified in subparagraph (A)(i) that, through the use of intermediaries with no or nominal operations or assets, or through other mechanisms, contrive to circumvent export controls for such items with respect to Iran.\n**(C)**\nA methodology for the Secretary of Commerce to proactively engage the United States manufacturers identified pursuant to the process under subparagraph (A)(ii), to provide such manufacturers with timely updates to the list of third-party distributors and resellers identified pursuant to the process under subparagraph (B).\n**(3) Submission**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Commerce shall submit to the appropriate congressional committees the strategy under paragraph (1).\n**(4) Form**\nThe report required by subsection (a)(1) shall be submitted in unclassified form, but portions of the report described in paragraphs (1) and (2) may contain a classified annex, so long as such annex is provided separately from the unclassified report.\n##### (b) Department of state strategy\n**(1) Strategy required**\nThe Secretary of State (in coordination with the Secretary of Commerce, the Secretary of Defense, and the Director of National Intelligence) shall develop a strategy to prevent the export to Iran of technologies from the United States and allied and partner countries which are used, or may be used, by Iran in the design, development, production, or operational employment of unmanned aircraft systems (including the microelectronics listed in subparagraphs (A) through (F) of subsection (a)(1)).\n**(2) Elements**\nThe strategy under paragraph (1) shall include, at a minimum, the following elements:\n**(A)**\nA process for the Secretary of State (in consultation with the relevant Secretaries and heads specified in paragraph (1)) to proactively identify foreign manufacturers of the technologies referred to in such paragraph.\n**(B)**\nA process for the Secretary of State to engage with any ally or partner of the United States regarding technologies which have been incorporated into an unmanned aircraft system produced by Iran, for the purpose of synchronizing the export control regime of such ally or partner with the United States export controls developed by the Secretary of Commerce pursuant to the strategy under subsection (a) with respect to such technology.\n**(3) Submission**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees the strategy under paragraph (1).\n**(4) Form**\nThe report required by subsection (b)(1) shall be submitted in unclassified form, but portions of the report described in paragraphs (1) and (2) may contain a classified annex, so long as such annex is provided separately from the unclassified report.\n##### (c) Requirement for secretary of defense To develop range of options\n**(1) In general**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Defense (in coordination with the Secretary of State and the Director of National Intelligence) shall develop a range of options that may be employed by the Armed Forces of the United States to counter or otherwise deny Iran the ability to acquire technologies used, or that may be used, in the design, development, production, or operational employment of unmanned aircraft systems by Iran, including the following technologies:\n**(A)**\nMicrocontrollers.\n**(B)**\nVoltage regulators.\n**(C)**\nDigital signal controllers.\n**(D)**\nGPS modules.\n**(E)**\nMicroprocessors.\n**(F)**\nComputer Aided Design (CAD) software.\n**(G)**\nComputer numerical control machines.\n**(2) Briefing**\nNot later than 45 days after the date of the enactment of this Act, the Secretary of Defense shall provide to the appropriate congressional committees a briefing on the options developed under paragraph (1).\n#### 5. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on Foreign Affairs, the Committee on Armed Services, and the Permanent Select Committee on Intelligence of the House of Representatives.\n**(B)**\nThe Committee on Foreign Relations, the Committee on Armed Services, the Committee on Banking, Housing, and Urban Affairs and the Permanent Select Committee on Intelligence of the Senate.\n**(2) Unmanned aircraft; unmanned aircraft system**\nThe terms unmanned aircraft and unmanned aircraft system have the meanings given those terms in section 130i of title 10, United States Code.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aviation and airports",
            "updateDate": "2025-08-05T17:07:47Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-08-05T17:07:55Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-05T17:08:02Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-08-05T17:08:09Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-08-05T17:08:17Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-08-05T17:08:23Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-08-05T17:08:30Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-08-05T17:08:43Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-08-05T17:08:58Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-08-05T17:09:09Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-08-05T17:09:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-19T19:35:05Z"
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
          "measure-id": "id119hr2505",
          "measure-number": "2505",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-09-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2505v00",
            "update-date": "2025-09-02"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Block the Use of Transatlantic Technology in Iranian Made Drones Act</strong></p><p>This bill requires the Departments of Commerce, State, and Defense to develop plans to prevent Iran from acquiring certain technologies related to unmanned aircraft systems (UAS), also known as drones.</p><p>Specifically, the bill requires Commerce to develop a strategy to prevent the illegal export to Iran of certain technologies (including microcontrollers, voltage regulators, and microprocessors) that can be used in the development and operation of UAS.</p><p>The State Department must develop a strategy to prevent the export of these technologies to Iran from the United States and allied and partner countries.</p><p>Finally, the Department of Defense must develop a range of options that may be employed by the U.S. Armed Forces to counter or deny the ability of Iran to acquire these technologies and other technologies useful for UAS, such as computer-aided design (CAD) software and computer numerical control (CNC) machines.</p>"
        },
        "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2505.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Block the Use of Transatlantic Technology in Iranian Made Drones Act</strong></p><p>This bill requires the Departments of Commerce, State, and Defense to develop plans to prevent Iran from acquiring certain technologies related to unmanned aircraft systems (UAS), also known as drones.</p><p>Specifically, the bill requires Commerce to develop a strategy to prevent the illegal export to Iran of certain technologies (including microcontrollers, voltage regulators, and microprocessors) that can be used in the development and operation of UAS.</p><p>The State Department must develop a strategy to prevent the export of these technologies to Iran from the United States and allied and partner countries.</p><p>Finally, the Department of Defense must develop a range of options that may be employed by the U.S. Armed Forces to counter or deny the ability of Iran to acquire these technologies and other technologies useful for UAS, such as computer-aided design (CAD) software and computer numerical control (CNC) machines.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119hr2505"
    },
    "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Block the Use of Transatlantic Technology in Iranian Made Drones Act</strong></p><p>This bill requires the Departments of Commerce, State, and Defense to develop plans to prevent Iran from acquiring certain technologies related to unmanned aircraft systems (UAS), also known as drones.</p><p>Specifically, the bill requires Commerce to develop a strategy to prevent the illegal export to Iran of certain technologies (including microcontrollers, voltage regulators, and microprocessors) that can be used in the development and operation of UAS.</p><p>The State Department must develop a strategy to prevent the export of these technologies to Iran from the United States and allied and partner countries.</p><p>Finally, the Department of Defense must develop a range of options that may be employed by the U.S. Armed Forces to counter or deny the ability of Iran to acquire these technologies and other technologies useful for UAS, such as computer-aided design (CAD) software and computer numerical control (CNC) machines.</p>",
      "updateDate": "2025-09-02",
      "versionCode": "id119hr2505"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2505ih.xml"
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
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-09-04T02:08:18Z"
    },
    {
      "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:52Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Block the Use of Transatlantic Technology in Iranian Made Drones Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the development of strategies and options to prevent the export to Iran of certain technologies related to unmanned aircraft systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:19Z"
    }
  ]
}
```
