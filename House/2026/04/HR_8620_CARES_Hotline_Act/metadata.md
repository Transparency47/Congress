# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8620
- Title: CARES Hotline Act
- Congress: 119
- Bill type: HR
- Bill number: 8620
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T20:57:34Z
- Update date including text: 2026-05-19T20:57:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8620",
    "number": "8620",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "CARES Hotline Act",
    "type": "HR",
    "updateDate": "2026-05-19T20:57:34Z",
    "updateDateIncludingText": "2026-05-19T20:57:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:07:30Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MS"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8620ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8620\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Menendez (for himself, Ms. Norton , Ms. Wilson of Florida , Mr. Thompson of Mississippi , Mr. Correa , and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Developmental Disabilities Assistance and Bill of Rights Act of 2000 to establish a hotline for caregivers of individuals with developmental disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Caregiver Access to Resources and Emotional Support Hotline Act or the CARES Hotline Act .\n#### 2. National Hotline for Caregivers of Individuals with Developmental Disabilities\n##### (a) In general\nThe Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15001 et seq. ) is amended by adding at the end the following:\nV Caregiver support 501. National Hotline for Caregivers of Individuals with Developmental Disabilities (a) In general The Secretary shall maintain, directly or by awarding a grant or entering into a contract with an eligible entity, a national hotline to provide emotional support, information, brief intervention, and mental health and resources to caregivers of individuals with developmental disabilities. (b) Requirements for hotline The hotline under subsection (a) shall\u2014 (1) be toll-free; (2) be a 24/7 real-time hotline; (3) provide voice and text support; (4) be staffed by trained personnel who receive standardized training in caregiver support, crisis response, and culturally and linguistically appropriate services; (5) include peer-to-peer staff who will work alongside the professionals specified in paragraph (4); (6) provide referral services to local, State, and Federal resources, including crisis support, adult services, transition programs, and in-home supports to meet the needs of caregivers, including family and household members, of individuals with developmental disabilities. (c) Additional requirements In maintaining the hotline under subsection (a), the Secretary (or eligible entity) shall\u2014 (1) consult with the Recognize, Assist, Include, Support, & Engage (RAISE) Family Caregivers Act Advisory Council to ensure that caregivers of individuals with developmental disabilities are connected in real-time to the appropriate specialized hotline service; (2) develop, maintain, and regularly update a national database of services, supports, and resources for caregivers of individuals with developmental disabilities. (d) Training program An eligible entity that receives a grant or enters into a contract to maintain the hotline under this section shall design, implement, and maintain training programs for the personnel described in subsection (b)(4). (e) Priority In making a grant or entering into a contract under this section, the Secretary shall give priority to entities that have in effect a partnership with a community-based organization. (f) Public awareness campaign The Secretary (or eligible entity) shall conduct national outreach and public awareness activities to raise awareness of the hotline through\u2014 (1) maintaining a public-facing website; and (2) developing and distributing educational and promotional materials. (g) Report Beginning not later than 1 year after the date of the enactment of this section, and annually thereafter, the Secretary shall submit a report to Congress on the hotline under subsection (a) and implementation of this section, including\u2014 (1) an evaluation of the effectiveness of activities conducted or supported under subsection (a); and (2) a directory of entities or organizations to which staff maintaining the hotline funded under this section may make referrals. (h) Eligible entity defined In this section, the term eligible entity means a nonprofit organization that has\u2014 (1) demonstrated national reach or capacity to serve all States and territories; and (2) experience navigating State-by-State service systems. (i) Authorization of appropriations To carry out this section, there are authorized to be appropriated $10,000,000 for each of fiscal years 2027 through 2032. .\n##### (b) Table of contents conforming amendment\nThe table of contents for such Act is amended by adding at the end the following:\nTitle V\u2014Caregiver Support Sec. 501. National Hotline for Caregivers of Individuals with Developmental Disabilities. .",
      "versionDate": "2026-04-30",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-05-19T20:57:34Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8620ih.xml"
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
      "title": "CARES Hotline Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARES Hotline Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Caregiver Access to Resources and Emotional Support Hotline Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Developmental Disabilities Assistance and Bill of Rights Act of 2000 to establish a hotline for caregivers of individuals with developmental disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:31Z"
    }
  ]
}
```
