# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6608
- Title: SHIELD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6608
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-10T08:05:47Z
- Update date including text: 2026-04-10T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6608",
    "number": "6608",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SHIELD Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:47Z",
    "updateDateIncludingText": "2026-04-10T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
            "date": "2025-12-11T16:10:20Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-11T05:00:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T05:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "LA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TN"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "WI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NE"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6608ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6608\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Arrington (for himself, Mr. Self , Mr. Higgins of Louisiana , Ms. Tenney , Mr. McCormick , Mr. Nehls , Mr. Burchett , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit Federal funds from being made available to any State or local government that arrests or prosecutes Federal law enforcement officers for performing duties related to the enforcement of Federal immigration law.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Homeland Immigration Enforcement from Local Detention Act of 2025 or as the SHIELD Act of 2025 .\n#### 2. Findings\nThe Congress finds as follows:\n**(1)**\nThe Constitution vests the Federal Government with exclusive authority over the enforcement of immigration laws.\n**(2)**\nFederal law enforcement officers acting within the scope of their duties must not be subject to arrest, detention, or prosecution by State or local jurisdictions for carrying out lawful immigration enforcement activities.\n**(3)**\nCertain jurisdictions have threatened or taken actions to impede Federal immigration enforcement, thereby undermining the rule of law and public safety.\n#### 3. Prohibition on Federal funds to jurisdictions that arrest or prosecute Federal officers\n##### (a) In general\nNo Federal financial assistance may be made available to a State or political subdivision thereof that\u2014\n**(1)**\narrests, detains, or prosecutes a Federal law enforcement officer; or\n**(2)**\notherwise interferes with or obstructs such officer, for actions taken by that officer in the lawful performance of their duties relating to the enforcement of Federal immigration law.\n##### (b) Determination\nThe Attorney General in consultation with the Secretary of Homeland Security, shall determine whether a State or unit of local government has engaged in conduct described in subsection (a).\n##### (c) Ineligibility\nFor fiscal year 2026, and each fiscal year thereafter, a State or political subdivision thereof determined to have engaged in the conduct described in subsection (a) at any time during the fiscal year is ineligible to receive Federal financial assistance for that fiscal year.\n##### (d) Reallocation\nAny Federal financial assistance that a State or political subdivision thereof is ineligible to receive pursuant to subsection (c) shall be reallocated to States or political subdivisions of States that are not ineligible under such section.\n##### (e) Definitions\nIn this Act:\n**(1)**\nThe term Federal financial assistance has the meaning given the term in section 7501 of title 31, United States Code.\n**(2)**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Northern Mariana Islands, the United States Virgin Islands, Guam, American Samoa, and any other territory or possession of the United States.\n#### 4. Restoration of funding\nFederal financial assistance withheld under section 3 shall be restored only if the Attorney General certifies the head of the Federal agency that administers such Federal financial assistance that the State or political subdivision thereof has ceased the offending conduct and has provided written assurances that such interference will not recur.\n#### 5. Definitions\nIn this Act:\n**(1)**\nThe term Federal law enforcement officer means any officer, agent, or employee authorized by the Department of Homeland Security, the Department of Justice, or any other Federal agency to enforce immigration laws.\n**(2)**\nThe term Federal funds includes any grant, contract, cooperative agreement, or other form of financial assistance provided by a Federal department or agency.\n#### 6. Effective date\nThis Act shall take effect on the date of enactment of this Act.",
      "versionDate": "2025-12-11",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-20T14:50:48Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6608ih.xml"
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
      "title": "SHIELD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHIELD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Homeland Immigration Enforcement from Local Detention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funds from being made available to any State or local government that arrests or prosecutes Federal law enforcement officers for performing duties related to the enforcement of Federal immigration law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T08:18:24Z"
    }
  ]
}
```
