# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/477
- Title: Fairness in Fentanyl Sentencing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 477
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/477",
    "number": "477",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Fairness in Fentanyl Sentencing Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
        "item": {
          "date": "2025-02-06T22:12:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SC"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s477is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 477\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Kennedy (for himself, Mr. Cruz , Mr. Graham , Mrs. Britt , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act and the Controlled Substances Import and Export Act to modify the offenses relating to fentanyl, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness in Fentanyl Sentencing Act of 2025 .\n#### 2. Controlled Substances Act amendments\nSection 401(b)(1) of the Controlled Substances Act ( 21 U.S.C. 841(b)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)(vi)\u2014\n**(A)**\nby striking 400 and inserting 20 ;\n**(B)**\nby striking 100 and inserting 5 ; and\n**(C)**\nby inserting scheduled or unscheduled before analogue of ; and\n**(2)**\nin subparagraph (B)(vi)\u2014\n**(A)**\nby striking 40 and inserting 2 ;\n**(B)**\nby striking 10 and inserting 0.5 ; and\n**(C)**\nby inserting scheduled or unscheduled before analogue of .\n#### 3. Controlled Substances Import and Export Act amendments\nSection 1010(b) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(F)\u2014\n**(A)**\nby striking 400 and inserting 20 ;\n**(B)**\nby striking 100 and inserting 5 ; and\n**(C)**\nby inserting scheduled or unscheduled before analogue of ; and\n**(2)**\nin paragraph (2)(F)\u2014\n**(A)**\nby striking 40 and inserting 2 ;\n**(B)**\nby striking 10 and inserting 0.5 ; and\n**(C)**\nby inserting scheduled or unscheduled before analogue of .\n#### 4. Directive to the Sentencing Commission\n##### (a) Definition\nIn this section, the term Commission means the United States Sentencing Commission.\n##### (b) Directive to the United States Sentencing Commission\nPursuant to the authority of the Commission under section 994(p) of title 28, United States Code, and in accordance with this section, the Commission shall review and amend, if appropriate, the guidelines and policy statements of the Commission applicable to a person convicted of an offense under section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ) or section 1010 of the Controlled Substances Import and Export Act ( 21 U.S.C. 960 ) to ensure that the guidelines and policy statements are consistent with the amendments made by sections 2 and 3 of this Act.\n##### (c) Emergency authority\nThe Commission shall\u2014\n**(1)**\npromulgate the guidelines, policy statements, or amendments provided for in this Act as soon as practicable, and in any event not later than 120 days after the date of enactment of this Act, in accordance with the procedure set forth in section 21(a) of the Sentencing Act of 1987 ( 28 U.S.C. 994 note), as though the authority under that Act had not expired; and\n**(2)**\npursuant to the emergency authority provided under paragraph (1), make such conforming amendments to the Federal sentencing guidelines as the Commission determines necessary to achieve consistency with other guideline provisions and applicable law.\n#### 5. Interdiction of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term chemical screening device means an immunoassay, narcotics field test kit, infrared spectrophotometer, mass spectrometer, nuclear magnetic resonance spectrometer, Raman spec\u00adtro\u00adpho\u00adto\u00adme\u00adter, or other scientific instrumentation able to collect data that can be interpreted to determine the presence of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances;\n**(2)**\nthe term express consignment operator or carrier has the meaning given the term in section 128.1 of title 19, Code of Federal Regulations, or any successor thereto; and\n**(3)**\nthe term Postmaster General means the Postmaster General of the United States Postal Service.\n##### (b) Interdiction of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances\n**(1) Chemical screening devices**\nThe Postmaster General shall\u2014\n**(A)**\nincrease the number of chemical screening devices that are available to the United States Postal Service; and\n**(B)**\nmake additional chemical screening devices available to the United States Postal Service as the Postmaster General determines are necessary to interdict fentanyl, other synthetic opioids, and other narcotics and psychoactive substances that are illegally imported into the United States, including such substances that are imported through the mail or by an express consignment operator or carrier.\n**(2) Personnel to interpret data**\nThe Postmaster General shall dedicate the appropriate number of personnel of the United States Postal Service, including scientists, so that those personnel are available during all operational hours to interpret data collected by chemical screening devices.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Postmaster General $9,000,000 to ensure that the United States Postal Service has resources, including chemical screening devices, personnel, and scientists, available during all operational hours to prevent, detect, and interdict the unlawful importation of fentanyl, other synthetic opioids, and other narcotics and psychoactive substances.",
      "versionDate": "2025-02-06",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-24T16:08:27Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-04-24T16:08:27Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-04-24T16:08:27Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-04-24T16:08:27Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-04-24T16:08:27Z"
          },
          {
            "name": "U.S. Sentencing Commission",
            "updateDate": "2025-04-24T16:08:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-12T16:31:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s477",
          "measure-number": "477",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s477v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fairness in Fentanyl Sentencing Act of 2025</strong></p><p>This bill modifies the drug quantity thresholds that trigger a mandatory minimum prison term for a defendant who manufactures, distributes, imports, exports, or possesses with intent to distribute fentanyl.</p><p>Specifically, the bill reduces from 400 to 20 grams the fentanyl quantity and from 100 to 5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for high-level first-time or repeat offenders. It also reduces from 40 to 2 grams the fentanyl quantity and from 10 to 0.5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for low-level first-time or repeat offenders.</p><p>Additionally, the bill directs the U.S. Postal Service to increase the availability of chemical screening devices and dedicate the appropriate number of personnel to interdict fentanyl and other substances that are unlawfully imported into the United States.</p>"
        },
        "title": "Fairness in Fentanyl Sentencing Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s477.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness in Fentanyl Sentencing Act of 2025</strong></p><p>This bill modifies the drug quantity thresholds that trigger a mandatory minimum prison term for a defendant who manufactures, distributes, imports, exports, or possesses with intent to distribute fentanyl.</p><p>Specifically, the bill reduces from 400 to 20 grams the fentanyl quantity and from 100 to 5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for high-level first-time or repeat offenders. It also reduces from 40 to 2 grams the fentanyl quantity and from 10 to 0.5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for low-level first-time or repeat offenders.</p><p>Additionally, the bill directs the U.S. Postal Service to increase the availability of chemical screening devices and dedicate the appropriate number of personnel to interdict fentanyl and other substances that are unlawfully imported into the United States.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s477"
    },
    "title": "Fairness in Fentanyl Sentencing Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness in Fentanyl Sentencing Act of 2025</strong></p><p>This bill modifies the drug quantity thresholds that trigger a mandatory minimum prison term for a defendant who manufactures, distributes, imports, exports, or possesses with intent to distribute fentanyl.</p><p>Specifically, the bill reduces from 400 to 20 grams the fentanyl quantity and from 100 to 5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for high-level first-time or repeat offenders. It also reduces from 40 to 2 grams the fentanyl quantity and from 10 to 0.5 grams the fentanyl analogue quantity that trigger a mandatory minimum prison term for low-level first-time or repeat offenders.</p><p>Additionally, the bill directs the U.S. Postal Service to increase the availability of chemical screening devices and dedicate the appropriate number of personnel to interdict fentanyl and other substances that are unlawfully imported into the United States.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s477"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s477is.xml"
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
      "title": "Fairness in Fentanyl Sentencing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness in Fentanyl Sentencing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act and the Controlled Substances Import and Export Act to modify the offenses relating to fentanyl, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:25Z"
    }
  ]
}
```
