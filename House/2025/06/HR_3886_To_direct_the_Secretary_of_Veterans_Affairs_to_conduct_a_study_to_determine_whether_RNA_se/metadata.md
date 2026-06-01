# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3886
- Title: Veterans PTSD Screening Act
- Congress: 119
- Bill type: HR
- Bill number: 3886
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2025-11-19T09:07:10Z
- Update date including text: 2025-11-19T09:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3886",
    "number": "3886",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Veterans PTSD Screening Act",
    "type": "HR",
    "updateDate": "2025-11-19T09:07:10Z",
    "updateDateIncludingText": "2025-11-19T09:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-23T18:16:00Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MP"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3886\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Murphy (for himself, Mrs. Kiggans of Virginia , and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to conduct a study to determine whether RNA sequencing can be used to effectively diagnose PTSD in veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans PTSD Screening Act .\n#### 2. Study of the Department of Veterans Affairs on RNA sequencing to diagnose PTSD in veterans\n##### (a) Establishment\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Veterans Affairs, acting through the Center for Innovation for Care and Payment of the Department of Veterans Affairs, shall conduct a study to determine whether RNA sequencing can be used to effectively diagnose veterans with inflammation or cellular stress, symptoms of post-traumatic stress disorder.\n##### (b) Locations\nThe Secretary shall carry out the study in medical facilities of the Department in five of the Veterans Integrated Service Networks.\n##### (c) Termination\nThe study shall terminate on September 30, 2027.\n##### (d) Report\nNot later than September 30, 2028, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report containing the results of the study.",
      "versionDate": "2025-06-10",
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
        "updateDate": "2025-06-24T20:26:56Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3886ih.xml"
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
      "title": "Veterans PTSD Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans PTSD Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to conduct a study to determine whether RNA sequencing can be used to effectively diagnose PTSD in veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:49:09Z"
    }
  ]
}
```
