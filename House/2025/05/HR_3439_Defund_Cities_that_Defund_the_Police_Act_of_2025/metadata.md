# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3439
- Title: Defund Cities that Defund the Police Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3439
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-06-12T08:06:56Z
- Update date including text: 2025-06-12T08:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3439",
    "number": "3439",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Defund Cities that Defund the Police Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:56Z",
    "updateDateIncludingText": "2025-06-12T08:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-15T21:16:49Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3439ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3439\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Fitzpatrick (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit a jurisdiction that defunds the police from receiving grants under certain Economic Development Assistance Programs and the Community Development Block Grant Program.\n#### 1. Short title\nThis Act may be cited as the Defund Cities that Defund the Police Act of 2025 .\n#### 2. Defunding jurisdiction defined\nIn this Act:\n**(1) Defunding State**\nThe term defunding State means a State that\u2014\n**(A)**\nabolishes or disbands a State law enforcement agency with no intention of reconstituting the State law enforcement agency; or\n**(B)**\nsignificantly reduces a State law enforcement agency\u2019s budget, provided that the State did not face a significant decrease in revenues in the previous fiscal year.\n**(2) Defunding locality**\nThe term defunding locality means a political subdivision of a State (other than a rural police department) that\u2014\n**(A)**\nis in an urbanized area, as defined by the United States Census Bureau; and\n**(B)**\n**(i)**\nabolishes or disbands the police department with no intention of reconstituting the jurisdiction\u2019s police department; or\n**(ii)**\nsignificantly reduces the police department\u2019s budget, provided that the jurisdiction did not face a significant decrease in revenues in the previous fiscal year.\n#### 3. Defunding jurisdictions ineligible for certain Federal funds\n##### (a) Economic development administration grants\n**(1) Grants for public works and economic development**\nSection 201(b) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3141(b) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking and at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(4) the area in which the project is to be carried out is not a defunding State or defunding locality (as defined in section 2 of the Defund Cities that Defund the Police Act of 2025 ). .\n**(2) Grants for planning and administrative expenses**\nSection 203(a) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3143(a) ) is amended by adding at the end the following: A defunding jurisdiction (as defined in section 2 of the Defund Cities that Defund the Police Act of 2025 ) may not be deemed an eligible recipient under this subsection. .\n**(3) Supplementary grants**\nSection 205(a) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3145(a) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking and at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(4) will be carried out in an area that does not contain a defunding State or defunding locality (as defined in section 2 of the Defund Cities that Defund the Police Act of 2025 ). .\n**(4) Grants for training, research, and technical assistance**\nSection 207 of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3147 ) is amended by adding at the end the following:\n(d) Ineligibility of defunding States or defunding localities Grant funds under this section may not be used to provide assistance to a defunding State or defunding locality (as defined in section 2 of the Defund Cities that Defund the Police Act of 2025 ). If a State is a defunding State during the period for which it receives amounts under this section, the Secretary shall direct the State to immediately return to the Secretary any such amounts that the State received for that period, and shall reallocate amounts returned for grants under this section to localities within the same State that are not defunding localities. .\n##### (b) Community development block grants\nTitle I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 102(a) ( 42 U.S.C. 5302(a) ), by adding at the end the following:\n(25) The term defunding State or locality has the meaning given such term in section 2 of the Defund Cities that Defund the Police Act of 2025 . ; and\n**(2)**\nin section 104 ( 42 U.S.C. 5304 )\u2014\n**(A)**\nsubsection (b)\u2014\n**(i)**\nin paragraph (5), by striking and at the end;\n**(ii)**\nby redesignating paragraph (6) as paragraph (7); and\n**(iii)**\nby inserting after paragraph (5) the following:\n(6) the grantee is not a defunding State or locality and will not become a defunding State or locality during the period for which the grantee receives a grant under this title; and ; and\n**(B)**\nby adding at the end the following:\n(n) Protection of individuals against crime (1) In general No funds made available to carry out this title may be obligated or expended for any State or unit of general local government that is a defunding State or locality. (2) Returned amounts (A) State If a State is a defunding State during the period for which it receives amounts under this title, the Secretary\u2014 (i) shall direct the State to immediately return to the Secretary any such amounts that the State received for that period; and (ii) shall reallocate amounts returned under clause (i) for grants under this title to localities within the same State that are not defunding localities. (B) Unit of general local government If a unit of general local government is a defunding locality during the period for which it receives amounts under this title, any such amounts that the unit of general local government received for that period\u2014 (i) in the case of a unit of general local government that is not in a nonentitlement area, shall be returned to the Secretary for grants under this title to States and other units of general local government that are not defunding localities; and (ii) in the case of a unit of general local government that is in a nonentitlement area, shall be returned to the Governor of the State for grants under this title to other units of general local government in the State that are not defunding localities. (C) Reallocation rules In reallocating amounts under subparagraphs (A) and (B), the Secretary shall\u2014 (i) apply the relevant allocation formula under subsection (b) or (d) of section 106, with all defunding States and localities excluded; and (ii) shall not be subject to the rules for reallocation under section 106(c). .",
      "versionDate": "2025-05-15",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-28T13:35:31Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3439ih.xml"
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
      "title": "Defund Cities that Defund the Police Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defund Cities that Defund the Police Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a jurisdiction that defunds the police from receiving grants under certain Economic Development Assistance Programs and the Community Development Block Grant Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:21Z"
    }
  ]
}
```
