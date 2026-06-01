# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3464
- Title: State Border Security Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 3464
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-16T08:08:04Z
- Update date including text: 2026-05-16T08:08:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3464",
    "number": "3464",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "State Border Security Assistance Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:04Z",
    "updateDateIncludingText": "2026-05-16T08:08:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-16",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-05-15T14:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-16T20:29:59Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:04:15Z",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
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
      "sponsorshipWithdrawnDate": "2025-06-05",
      "state": "ME"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3464ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3464\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Roy (for himself, Mr. Pfluger , Mr. Crenshaw , Mr. Ellzey , Mr. Golden of Maine , Mr. Weber of Texas , Mr. Moran , and Mr. McCaul ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the State Border Security Reinforcement Fund and the State Criminal Alien Prosecution and Detention Fund, to make appropriations to each of these funds, and to authorize the use of such amounts for grants to eligible States, State agencies, and units of local government for specified purposes.\n#### 1. Short title\nThis Act may be cited as the State Border Security Assistance Act .\n#### 2. State border security reinforcement fund\n##### (a) Establishment of fund\nThere is established, in the Department of Homeland Security, a fund, which shall be known as the State Border Security Reinforcement Fund (referred to in this section as the Fund ). The Secretary of Homeland Security shall use amounts appropriated or otherwise made available for the Fund for grants to eligible States, State agencies, including National Guard units, and units of local government for any of the following purposes:\n**(1)**\nConstruction or installation of a border wall, border fencing, or other barriers or buoys along the southern border of the United States, which may include planning, procurement of materials, and personnel costs related to such construction.\n**(2)**\nAny work necessary to prepare the ground at or near the United States border to allow construction or maintenance of a border wall or other barrier fencing or effective surveillance.\n**(3)**\nInformation-gathering and surveillance to detect and interdict the unlawful entry of persons or contraband across the United States border.\n**(4)**\nRelocation of aliens who are unlawfully present in the United States from small population centers.\n##### (b) Appropriation\nIn addition to amounts otherwise available for the purposes described in paragraphs (1) through (4) of subsection (a), there is appropriated in fiscal year 2025, out of any money in the Treasury not otherwise appropriated, to the Department of Homeland Security for the Fund, $11,000,000,000, to remain available until September 30, 2034, for qualified expenses that meet the purposes described in subsection (a).\n##### (c) Grant eligibility of completed, ongoing, or new activities\nThe Secretary of Homeland Security may provide grants under subsection (a) to State agencies and units of local government for expenditures they made for completed, ongoing, or new activities determined to be eligible for such grant funding that occurred on or after January 20, 2021.\n##### (d) Sunset\nThe Fund shall terminate on January 20, 2029, and any unobligated amounts remaining in the Fund on that date shall be returned to the Treasury of the United States for deficit reduction purposes.\n#### 3. State criminal alien prosecution and detention fund\n##### (a) Establishment of fund\nThere is established, in the Department of Justice, a fund, which shall be known as the State Criminal Alien Prosecution and Detention Fund (referred to in this section as the Fund ). The Attorney General shall use amounts appropriated or otherwise made available for the Fund for grants to eligible States, State agencies, including National Guard units, and units of local government for any of the following purposes:\n**(1)**\nLocating and apprehending aliens who are unlawfully present in the United States or have committed a crime under Federal, State, or local law.\n**(2)**\nIntelligence and information-gathering to counter gang activity.\n**(3)**\nInvestigating and prosecuting crimes committed by aliens and drug and human trafficking crimes.\n**(4)**\nCourt operations related to the prosecution of crimes committed by aliens and drug and human trafficking crimes.\n**(5)**\nTemporarily detaining aliens, including costs related to facility operations, personnel, and health and safety related services.\n**(6)**\nTransporting aliens described in paragraph (1) to locations related to their apprehension, detention, and prosecution.\n**(7)**\nVehicle maintenance, logistics, transportation, and other support provided to law enforcement agencies by a State agency to enhance their ability to locate and apprehend aliens who have unlawfully entered the United States or have committed crimes under Federal, State, or local law.\n##### (b) Appropriation\nIn addition to amounts otherwise available for the purposes described in paragraphs (1) through (6) of subsection (a), there is appropriated in fiscal year 2025, out of any money in the Treasury not otherwise appropriated, to the Department of Justice for the Fund, $3,500,000,000, to remain available until September 30, 2034, for qualified expenses that achieve any such purposes.\n##### (c) Grant eligibility of completed, ongoing, or new activities\nThe Attorney General may provide grants under subsection (a) to State agencies and units of local government for expenditures they made for completed, ongoing, or new activities determined to be eligible for such grant funding that occurred on or after January 20, 2021.\n##### (d) Sunset\nThe Fund shall terminate on January 20, 2029, and any unobligated amounts remaining in the Fund on that date shall be returned to the Treasury of the United States for deficit reduction purposes.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-15",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1790",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "State Border Security Assistance Act",
      "type": "S"
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
        "name": "Immigration",
        "updateDate": "2025-05-28T17:33:32Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3464ih.xml"
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
      "title": "State Border Security Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Border Security Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the State Border Security Reinforcement Fund and the State Criminal Alien Prosecution and Detention Fund, to make appropriations to each of these funds, and to authorize the use of such amounts for grants to eligible States, State agencies, and units of local government for specified purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:26Z"
    }
  ]
}
```
