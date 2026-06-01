# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5589
- Title: To name the Department of Veterans Affairs clinic located in Riverhead, New York, as the "Private First Class Garfield M. Langhorn VA Clinic", and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5589
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-04-16T08:06:44Z
- Update date including text: 2026-04-16T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-15 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-15 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5589",
    "number": "5589",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "To name the Department of Veterans Affairs clinic located in Riverhead, New York, as the \"Private First Class Garfield M. Langhorn VA Clinic\", and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:44Z",
    "updateDateIncludingText": "2026-04-16T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-15",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-15T18:49:40Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
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
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5589ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5589\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. LaLota (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo name the Department of Veterans Affairs clinic located in Riverhead, New York, as the Private First Class Garfield M. Langhorn VA Clinic , and for other purposes.\n#### 1. Findings\nCongress finds the following:\n**(1)**\nGarfield McConnell Langhorn was born on September 10, 1948, in Cumberland, Virginia, and grew up in Riverhead, New York, on Long Island.\n**(2)**\nLanghorn graduated from Riverside High School in 1967, and worked for Suffolk County before being drafted into the United States Army in 1968. Private First Class Langhorn was assigned as a radio operator with Troop C, 7th Squadron (Airmobile), 17th Cavalry Regiment, 1st Aviation Brigade, and deployed to Vietnam in November 1968.\n**(3)**\nOn January 15, 1969, Langhorn\u2019s unit was inserted near Plei Djereng, Pleiku Province, to rescue downed AH\u20131 Cobra helicopter pilots. After finding both pilots deceased, the unit came under heavy attack by North Vietnamese forces in heavily fortified positions. Amid intense combat and while surrounded, Langhorn radioed for urgent air support, coordinating minigun and rocket strikes from the gunships above, and provided covering fire from within the defensive perimeter.\n**(4)**\nAs darkness fell and air support became ineffective, enemy soldiers began probing the perimeter. When an enemy grenade landed close to wounded comrades, Langhorn unhesitatingly threw himself on the grenade, scooped it beneath his body, and absorbed the blast. By sacrificing himself, he saved the lives of his comrades.\n**(5)**\nPrivate First Class Langhorn\u2019s selfless act of valor, in giving his life to save his fellow soldiers, stands as a timeless example of courage and sacrifice that continues to inspire his community and our Nation.\n#### 2. Name of Department of Veterans Affairs clinic, Bay Shore, New York\nThe Department of Veterans Affairs clinic located in Riverhead, New York, shall, after the date of the enactment of this Act, be known and designated as the Private First Class Garfield M. Langhorn VA Clinic . Any reference to such clinic in any law, regulation, map, document, record, or other paper of the United States shall be considered to be a reference to the Private First Class Garfield M. Langhorn VA Clinic .",
      "versionDate": "2025-09-26",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:43:44Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5589ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To name the Department of Veterans Affairs clinic located in Riverhead, New York, as the \"Private First Class Garfield M. Langhorn VA Clinic\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T07:33:37Z"
    },
    {
      "title": "To name the Department of Veterans Affairs clinic located in Riverhead, New York, as the \"Private First Class Garfield M. Langhorn VA Clinic\", and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T08:05:36Z"
    }
  ]
}
```
