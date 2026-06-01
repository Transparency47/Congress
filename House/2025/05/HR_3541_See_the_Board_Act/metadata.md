# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3541
- Title: See the Board Act
- Congress: 119
- Bill type: HR
- Bill number: 3541
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3541",
    "number": "3541",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "See the Board Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-21T14:03:35Z",
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
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DC"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "PA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3541ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3541\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mrs. Hayes (for herself, Ms. Simon , Mr. Cohen , Ms. Norton , Mr. Takano , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for a grant program to support access to free eye care services for students attending public elementary schools and secondary schools.\n#### 1. Short title\nThis Act may be cited as the See the Board Act .\n#### 2. Grant program to support access to free eye care services for students at public schools\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall, subject to subsection (d), establish a grant program under which the Secretary awards grants to eligible entities that provide a qualifying eye care services program to purchase portable or mobile eye care equipment and to pay for appropriate operational costs, including for costs for qualified personal protective equipment, direct health care or service delivery costs, and any other relevant expense the Secretary determines necessary, for the provision of free eye care services through such program to students attending public elementary schools or secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )).\n##### (b) Eligible entities described\nFor purposes of this section, an eligible entity is a nonprofit organization.\n##### (c) Qualifying eye care services program\nFor purposes of this section, the term qualifying eye care services program means a program under which such services are furnished free of charge to students attending public elementary schools or secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) through the use of mobile eye clinics or mobile clinics that use portable equipment to bring screenings, exams, and an optical shop to such students. Such a program may use qualified health care providers at such schools or ophthalmic technicians for screening, optometrists or ophthalmologists for follow-up examinations, and an optician and dispensary for such students to be given glasses at such schools.\n##### (d) Sense of Congress\nIt is the sense of Congress that eligible entities awarded grants under this section should, to the greatest extent possible, provide information to students described in subsection (a) and parents of such students about the importance of adhering to the medically recommended schedule for vision screenings and comprehensive eye exams.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-05-21",
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
        "name": "Education",
        "updateDate": "2025-05-30T14:15:11Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3541ih.xml"
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
      "title": "See the Board Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T07:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "See the Board Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T07:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a grant program to support access to free eye care services for students attending public elementary schools and secondary schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T07:03:58Z"
    }
  ]
}
```
