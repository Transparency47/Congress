# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6490
- Title: To direct the Secretary of Defense to establish a pilot program to provide certain members of the Armed Forces with timely and relevant information via text message, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6490
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-01-22T09:06:26Z
- Update date including text: 2026-01-22T09:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6490",
    "number": "6490",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "To direct the Secretary of Defense to establish a pilot program to provide certain members of the Armed Forces with timely and relevant information via text message, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-01-22T09:06:26Z",
    "updateDateIncludingText": "2026-01-22T09:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:15Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NE"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "NV"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "VA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "NH"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
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
      "sponsorshipDate": "2026-01-21",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6490ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6490\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Ms. Houlahan (for herself, Mrs. Kiggans of Virginia , Mr. Bacon , Mr. Horsford , Mr. Wittman , and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to establish a pilot program to provide certain members of the Armed Forces with timely and relevant information via text message, and for other purposes.\n#### 1. Pilot program for push-text notifications to members and dependents\n##### (a) Establishment\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall establish a pilot program to be known as the Push-Text Initiative (in this section referred to as the pilot program ) to provide members of the Armed Forces assigned to Marine Corps Installations Pacific in Okinawa, Japan, and the adult dependents of such members with timely and relevant information via text message.\n##### (b) Implementation\nThe pilot program shall\u2014\n**(1)**\nautomatically enroll all eligible members of the Armed Force assigned to the locations participating in the pilot program and the dependents of such members using all available text messaging contact information provided by such members; and\n**(2)**\nprovide all recipients with the ability to opt out of receiving text messages under the pilot program at any time.\n##### (c) Covered information\nText messages transmitted under the pilot program shall include\u2014\n**(1)**\ninformation on military spouse employment opportunities, career counseling, and related support programs;\n**(2)**\nupdates with respect to childcare services available both on and off the installation, availability of child care, and child care fee assistance programs;\n**(3)**\ninformation regarding general TRICARE program benefits, enrollment deadlines, and other health-related resources;\n**(4)**\nnotifications of changes in Department of Defense policies, regulations, or Federal laws that affect members or dependents of members; and\n**(5)**\nany other information or resources that the Secretary considers relevant to the well-being of members and dependents of members.\n##### (d) Report\nNot later than October 1, 2027, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and House of Representatives a report on the pilot program. Such report shall include\u2014\n**(1)**\na description of how the pilot program was implemented, including the timeline, execution plan, and the official managing the pilot program;\n**(2)**\ndata on participation and usage, including the number of individuals automatically enrolled, the opt-out rate, and the frequency and types of messages transmitted;\n**(3)**\nany observed benefits or outcomes of the pilot program, including feedback from participants;\n**(4)**\nan analysis of the costs of operating the pilot program and any cost savings or efficiencies achieved by consolidating or scaling back other outreach efforts with respect to issues addressed by the pilot program; and\n**(5)**\nthe recommendations of the Secretary with respect to the feasibility and advisability of continuing or expanding the pilot program to the entire Department of Defense, including any proposed modifications to the program and an assessment of the anticipated costs, resource requirements, and potential benefits of Department-wide implementation.",
      "versionDate": "2025-12-05",
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
        "updateDate": "2025-12-17T15:34:52Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6490ih.xml"
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
      "title": "To direct the Secretary of Defense to establish a pilot program to provide certain members of the Armed Forces with timely and relevant information via text message, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:22Z"
    },
    {
      "title": "To direct the Secretary of Defense to establish a pilot program to provide certain members of the Armed Forces with timely and relevant information via text message, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-06T09:05:57Z"
    }
  ]
}
```
