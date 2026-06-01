# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8367
- Title: Answering the Call Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8367
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-15T13:04:34Z
- Update date including text: 2026-05-15T13:04:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-13 - IntroReferral: Sponsor introductory remarks on measure. (CR H3446)
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-13 - IntroReferral: Sponsor introductory remarks on measure. (CR H3446)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8367",
    "number": "8367",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Answering the Call Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-15T13:04:34Z",
    "updateDateIncludingText": "2026-05-15T13:04:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3446)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8367ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8367\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mrs. Cammack introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to enhance outreach to first responders in the implementation of the National Suicide Prevention Lifeline program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Answering the Call Act of 2026 .\n#### 2. National Suicide Prevention Lifeline program: outreach to first responders\n##### (a) In general\nSection 520E\u20133 of the Public Health Service Act ( 42 U.S.C. 290bb\u201336c ) is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h); and\n**(2)**\nby inserting after subsection (f) the following:\n(g) Outreach to first responders (1) In general The Secretary shall conduct outreach activities to address barriers to use of the 9\u20138\u20138 national suicide hotline by first responders, including stigma, lack of tailored services, and privacy concerns. (2) Activities For purposes of paragraph (1), the Secretary shall\u2014 (A) in coordination with first responder organizations, carry out programs and activities to promote the 9\u20138\u20138 national suicide hotline as a key mental health resource for first responders; (B) award grants, contracts, or cooperative agreements to support public awareness campaigns that integrate information about the 9\u20138\u20138 national suicide hotline into first responder training programs, wellness policies, and resources maintained by labor organizations; (C) collect data on the use of the 9\u20138\u20138 national suicide hotline by first responders to measure the impact of the hotline and inform future outreach strategies of the Secretary; and (D) develop and disseminate training programs for counselors and other staff of the 9\u20138\u20138 national suicide hotline that incorporate evidence-based, trauma-informed, and behavioral-health-focused best practices that are specific to first responders. (3) Privacy protections In collecting data under paragraph (2)(C), the Secretary\u2014 (A) shall ensure that the data collected is administered in a manner that protects personal privacy, consistent with applicable Federal and State privacy laws, including through aggregation and de-identification of the data; (B) shall focus on identifying trends in presenting issues and utilization of the 9\u20138\u20138 national suicide hotline for populations served among first responders, rather than collecting personally identifiable information; and (C) may work in collaboration with State and local partners and use existing public health reporting mechanisms. (4) Definitions In this subsection: (A) First responder The term first responder includes law enforcement officers, firefighters, emergency medical technicians, and public safety telecommunicators. (B) First responder organization The term first responder organization includes national, State, local, Tribal, and nonprofit firefighter, law enforcement, emergency medical services, and public safety telecommunicator organizations that are recognized for their experience and expertise in fire prevention and safety programs and activities, including labor organizations, professional associations, and peer support and behavioral health organizations serving first responders. .\n##### (b) First responder organizations collaboration pilot program\n**(1) In general**\nThe Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, shall conduct a pilot program to provide for collaboration between\u2014\n**(A)**\nthe Substance Abuse and Mental Health Services Administration;\n**(B)**\nthe United States Fire Administration; and\n**(C)**\nfirst responder organizations.\n**(2) Purpose**\nThe purpose of the pilot program shall be to ensure that outreach activities conducted under section 520E\u20133(g) of the Public Health Service Act (as inserted by subsection (a) of this section) are appropriately tailored to increase awareness of the 9\u20138\u20138 national suicide hotline among first responders.\n**(3) Report to Congress**\nNot later than 3 years after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report on the results of the pilot program conducted under this subsection.\n**(4) Definitions**\nThe definitions in section 520E\u20133(g) of the Public Health Service Act (as inserted by subsection (a) of this section) shall apply to this subsection.",
      "versionDate": "2026-04-20",
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
        "name": "Health",
        "updateDate": "2026-04-30T20:00:42Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8367ih.xml"
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
      "title": "Answering the Call Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Answering the Call Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to enhance outreach to first responders in the implementation of the National Suicide Prevention Lifeline program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:31Z"
    }
  ]
}
```
