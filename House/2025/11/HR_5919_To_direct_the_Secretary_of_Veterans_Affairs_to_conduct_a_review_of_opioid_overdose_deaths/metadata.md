# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5919
- Title: Veterans HOPE Act
- Congress: 119
- Bill type: HR
- Bill number: 5919
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-04-08T17:51:42Z
- Update date including text: 2026-04-08T17:51:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5919",
    "number": "5919",
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
    "title": "Veterans HOPE Act",
    "type": "HR",
    "updateDate": "2026-04-08T17:51:42Z",
    "updateDateIncludingText": "2026-04-08T17:51:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
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
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CT"
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
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5919ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5919\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Murphy (for himself and Mr. Courtney ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to conduct a review of opioid overdose deaths among veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Heroin Overdose Prevention Examination Act or the Veterans HOPE Act .\n#### 2. Findings; Sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nNew research shows that a dramatic rise in opioid overdose deaths among veterans in recent years has happened increasingly among veterans dying from heroin and synthetic opioids.\n**(2)**\nFurthermore, patients of the Veterans Health Administration of the Department of Veterans Affairs are seven times more likely to suffer from an opioid use disorder than commercially insured patients.\n**(3)**\nUsing records of the Veterans Health Administration linked to National Death Index data, the veterans\u2019 rate of overdose deaths from all opioids increased by 65 percent from 2010 to 2016, a rate change that includes adjustments for demographic changes in the veteran population over time.\n**(4)**\nFurthermore, among all opioid overdose decedents, prescription opioid receipt within three months before death declined from 54 percent in 2010 to 26 percent in 2016, yet veteran overdoses resulting in death from heroin, synthetic opioids such as fentanyl, and nonprescription opioids still occurred.\n**(5)**\nIn fact, between 2010 and 2016, the veteran death rate from heroin or from taking multiple opioids almost quintupled and the death rate from synthetic opioids such as fentanyl increased by more than five-fold.\n**(6)**\nTrends would suggest that, while the aggregate rise in opioid overdose deaths among veterans parallel those seen in the general population, the increase occurred mainly because of a rise in deaths from nonprescribed sources such as heroin, fentanyl, other powerful synthetic opioids, or multiple opioids in concurrent use.\n##### (b) Sense of Congress\nIt is the sense of Congress that further veterans overdose prevention efforts and research should extend beyond patients actively receiving opioid prescriptions.\n#### 3. Review of deaths of veterans relating to opioid use\n##### (a) Review\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall complete a review of the deaths of all covered veterans who died from opioid overdoses during the five-year period preceding the date of the enactment for this Act.\n##### (b) Matters included\nThe review under subsection (a) shall include the following:\n**(1)**\nThe total number of covered veterans who died from opioid overdoses during the five-year period preceding the date of the enactment of this Act.\n**(2)**\nA summary of such veterans that includes the age, sex, race, and ethnicity of each such veteran.\n**(3)**\nA comprehensive list of the medications prescribed to, and found in the bodies of, such veterans at the time of death, specifically listing any medications that carry a black box warning, are off-label, or are psychotropic.\n**(4)**\nA summary of medical diagnoses by physicians of the Department of Veterans Affairs that led to any prescribing of the medications referred to in paragraph (3).\n**(5)**\nThe number of instances in which such a veteran was concurrently on multiple medications prescribed by physicians of the Department.\n**(6)**\nA summary of\u2014\n**(A)**\nthe average period that elapsed between the last prescription opioid receipt and the date of the death of such a veteran; and\n**(B)**\nthe cause of death for each such veteran.\n**(7)**\nThe percentage of such veterans with combat experience or trauma (including military sexual trauma, traumatic brain injury, and post-traumatic stress).\n**(8)**\nIdentification of medical facilities of the Department with high prescription and drug abuse treatment rates for patients being treated at those facilities.\n**(9)**\nA description of policies of the Department governing the prescribing of medications referred to in paragraph (3).\n**(10)**\nA description of efforts by the Secretary to electronically track, collect, and properly dispose of prescription opioids that are either unused, past the prescription date, or not in the possession of the properly prescribed patient.\n**(11)**\nA description of any patterns apparent to the Secretary based on the review.\n**(12)**\nRecommendations for further action that would improve the safety and well-being of veterans and reduce opioid overdose rates for veterans, especially concerning research regarding such veterans who had not filed for a opioid prescription in the three months before death by overdose.\n##### (c) Public availability\nNot later than 45 days after the completion of the review under subsection (a), the Secretary shall\u2014\n**(1)**\nsubmit to Congress a report on the results of the review;\n**(2)**\nmake such report publicly available; and\n**(3)**\nprovide to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a briefing on such review.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term black box warning means a warning displayed within a box in the prescribing information for drugs that have special problems, particularly ones that may lead to death or serious injury.\n**(2)**\nThe term covered veteran means any veteran who received hospital care or medical services furnished by the Department of Veterans Affairs during the five-year period preceding the death of the veteran.",
      "versionDate": "2025-11-04",
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
        "updateDate": "2025-11-18T15:56:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-04",
    "originChamber": "House",
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
          "measure-id": "id119hr5919",
          "measure-number": "5919",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5919v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Veterans Heroin Overdose Prevention Examination Act or the Veterans HOPE Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died from opioid overdoses during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>"
        },
        "title": "Veterans HOPE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5919.xml",
    "summary": {
      "actionDate": "2025-11-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veterans Heroin Overdose Prevention Examination Act or the Veterans HOPE Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died from opioid overdoses during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5919"
    },
    "title": "Veterans HOPE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Veterans Heroin Overdose Prevention Examination Act or the Veterans HOPE Act</b></p> <p>This bill requires the Department of Veterans Affairs (VA) to complete a review of the deaths of all covered veterans who died from opioid overdoses during the five-year period preceding the enactment of this bill. Covered veterans are those who received VA hospital care or medical services during the five-year period preceding the death of the veteran. </p> <p>The VA shall report on the results of the review and make such report publicly available.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5919"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5919ih.xml"
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
      "title": "Veterans HOPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans HOPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Heroin Overdose Prevention Examination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to conduct a review of opioid overdose deaths among veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:15Z"
    }
  ]
}
```
