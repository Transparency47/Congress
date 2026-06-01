# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/800
- Title: Precision Brain Health Research Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 800
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-04-10T16:58:16Z
- Update date including text: 2026-04-10T16:58:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/800",
    "number": "800",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Precision Brain Health Research Act of 2025",
    "type": "S",
    "updateDate": "2026-04-10T16:58:16Z",
    "updateDateIncludingText": "2026-04-10T16:58:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-07-30T20:00:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-30T20:00:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:20Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:20Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-27T20:44:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "SD"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s800is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 800\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Moran (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo modify the Precision Medicine for Veterans Initiative of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Precision Brain Health Research Act of 2025 .\n#### 2. Modification of Precision Medicine for Veterans Initiative\nSection 305 of the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 ( 38 U.S.C. 1712A note; Public Law 116\u2013171 ) is amended\u2014\n**(1)**\nin subsection (a), by striking and such other mental health conditions and inserting repetitive low-level blast exposure, dementia, and such other brain and mental health conditions ;\n**(2)**\nin subsection (d)(4), by adding at the end the following new subparagraph:\n(E) Data-sharing partnership (i) In general The Secretary shall work with the Secretary of Defense to establish a data-sharing partnership between the Department of Veterans Affairs and the Department of Defense. (ii) Storage The partnership established under clause (i) shall be stored in the open platform made available under this paragraph. (iii) Data The data supplied by the Secretary of Defense shall include all relevant data, Department-wide, collected through\u2014 (I) the United States Armed Forces; (II) the United States Special Operations Command; and (III) the Long-Term Impact of Military-Relevant Brain Injury Consortium Chronic Effects of Neurotrauma Consortium maintained by the Defense Health Agency. ; and\n**(3)**\nby adding at the end the following new subsections:\n(f) Repetitive low-Level blast exposure research In carrying out the initiative under subsection (a), the Secretary of Veterans Affairs shall conduct the following research: (1) A big-data assessment of the clinical and non-clinical interventions that are illustrating positive outcomes for patients within the health system of the Veterans Health Administration with likely low-level repetitive blast injuries, including a categorization of military occupational specialties, and units, known to experience higher levels of low-level repetitive blast injuries. (2) Not fewer than two large-scale implementation studies of research-proven interventions within such health system for patients with likely low-level repetitive blast injuries, including a categorization of military occupational specialties, and units, known to experience higher levels of low-level repetitive blast injuries. (3) A translational research study on the use of growth hormone replacement therapy on the improvement of cognitive function, quality of life, brain structure, and other negative symptoms on patients within such health system with likely low-level repetitive blast injuries. (4) Not fewer than four large-scale quality improvement studies on improving the diagnosis and care of veteran patients with likely low-level repetitive blast injuries. (g) Assistance and report by National Academies of Sciences, Engineering, and Medicine Not later than 60 days after the date of the enactment of the Precision Brain Health Research Act of 2025 , the Secretary of Veterans Affairs shall seek to enter into a contract with the National Academies of Sciences, Engineering, and Medicine under which the National Academies shall\u2014 (1) work in tandem with the initiative under subsection (a) on validation of brain and mental health biomarkers among veterans; and (2) not less frequently than once every two years, submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the work completed under paragraph (1). (h) Assessment (1) In general The Secretary of Veterans Affairs shall conduct an assessment of all translational research studies in progress and planned under the initiative under subsection (a), including research under subsection (f). (2) Report Not later than 60 days after completion of the assessment conducted under paragraph (1), the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the assessment. (i) Reports (1) In general Not less frequently than once every two years, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the initiative under subsection (a). (2) Recommendations Each report required by paragraph (1) shall include recommendations for immediate administrative and legislative action to improve the initiative under subsection (a). (j) Authorization of appropriations There is authorized to be appropriated to the Secretary of Veterans Affairs $5,000,000 to carry out the initiative under subsection (a) for each of fiscal years 2025 through 2034. .",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-02T20:28:04Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:58:16Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-02T20:27:42Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-06-02T20:27:36Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-06-02T20:27:15Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-06-02T20:27:20Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-06-02T20:27:59Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-06-02T20:27:25Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-02T20:26:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:59:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "Senate",
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
          "measure-id": "id119s800",
          "measure-number": "800",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-07-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s800v00",
            "update-date": "2025-07-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Precision Brain Health Research Act of 2025</strong></p><p>This bill expands the Scott Hannon Initiative for Precision Mental Health, a program at the Department of Veterans Affairs (VA).</p><p>Specifically, the bill expands the scope of the initiative by requiring the identification and validation of brain and mental health\u00a0biomarkers among veterans for repetitive low-level blast exposure, dementia, and other such brain conditions. Currently, the initiative addresses several other conditions such as depression and post-traumatic stress disorder.</p><p>The VA must work with the Department of Defense to establish a data-sharing partnership under the initiative.</p><p>The bill requires the VA to conduct various research studies about repetitive low-level blast exposure under the initiative.</p><p>The VA must seek to enter into a contract with the National Academies of Sciences, Engineering, and Medicine to work in tandem with the initiative on validation of brain and mental health\u00a0biomarkers among veterans and report on the findings at least once every two years.</p><p>The VA must assess all in progress and planned translational research studies under the initiative and report to Congress on the assessment.</p><p>Additionally, the VA must report to Congress on the initiative at least once every two years and include recommendations for immediate administrative and legislative action to improve the initiative.</p><p>The bill authorizes the initiative through FY2034.</p>"
        },
        "title": "Precision Brain Health Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s800.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Precision Brain Health Research Act of 2025</strong></p><p>This bill expands the Scott Hannon Initiative for Precision Mental Health, a program at the Department of Veterans Affairs (VA).</p><p>Specifically, the bill expands the scope of the initiative by requiring the identification and validation of brain and mental health\u00a0biomarkers among veterans for repetitive low-level blast exposure, dementia, and other such brain conditions. Currently, the initiative addresses several other conditions such as depression and post-traumatic stress disorder.</p><p>The VA must work with the Department of Defense to establish a data-sharing partnership under the initiative.</p><p>The bill requires the VA to conduct various research studies about repetitive low-level blast exposure under the initiative.</p><p>The VA must seek to enter into a contract with the National Academies of Sciences, Engineering, and Medicine to work in tandem with the initiative on validation of brain and mental health\u00a0biomarkers among veterans and report on the findings at least once every two years.</p><p>The VA must assess all in progress and planned translational research studies under the initiative and report to Congress on the assessment.</p><p>Additionally, the VA must report to Congress on the initiative at least once every two years and include recommendations for immediate administrative and legislative action to improve the initiative.</p><p>The bill authorizes the initiative through FY2034.</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119s800"
    },
    "title": "Precision Brain Health Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Precision Brain Health Research Act of 2025</strong></p><p>This bill expands the Scott Hannon Initiative for Precision Mental Health, a program at the Department of Veterans Affairs (VA).</p><p>Specifically, the bill expands the scope of the initiative by requiring the identification and validation of brain and mental health\u00a0biomarkers among veterans for repetitive low-level blast exposure, dementia, and other such brain conditions. Currently, the initiative addresses several other conditions such as depression and post-traumatic stress disorder.</p><p>The VA must work with the Department of Defense to establish a data-sharing partnership under the initiative.</p><p>The bill requires the VA to conduct various research studies about repetitive low-level blast exposure under the initiative.</p><p>The VA must seek to enter into a contract with the National Academies of Sciences, Engineering, and Medicine to work in tandem with the initiative on validation of brain and mental health\u00a0biomarkers among veterans and report on the findings at least once every two years.</p><p>The VA must assess all in progress and planned translational research studies under the initiative and report to Congress on the assessment.</p><p>Additionally, the VA must report to Congress on the initiative at least once every two years and include recommendations for immediate administrative and legislative action to improve the initiative.</p><p>The bill authorizes the initiative through FY2034.</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119s800"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s800is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Precision Brain Health Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Precision Brain Health Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the Precision Medicine for Veterans Initiative of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:17Z"
    }
  ]
}
```
