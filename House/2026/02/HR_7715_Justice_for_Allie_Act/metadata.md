# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7715?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7715
- Title: Justice for Allie Act
- Congress: 119
- Bill type: HR
- Bill number: 7715
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-05-30T08:06:02Z
- Update date including text: 2026-05-30T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7715",
    "number": "7715",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Justice for Allie Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:02Z",
    "updateDateIncludingText": "2026-05-30T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:00:35Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "MI"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "MI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7715ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7715\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Ms. Stevens (for herself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit coercing protected adults to send or otherwise transmit an intimate visual depiction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Allie Act .\n#### 2. Sexual exploitation of protected adults\n##### (a) In general\nChapter 109A of title 18, United States Code, is amended by adding at the end the following:\n2245A. Sexual exploitation of protected adults (a) Offense Whoever, using the mail or any facility or means of interstate or foreign commerce, knowingly persuades, induces, entices, or coerces any protected adult to send or otherwise transmit an intimate visual depiction (as such term is defined in section 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 )) with the intent to harm such protected adult, or attempts to do so\u2014 (1) in the case of a first offense under this section, shall be fined under this title, imprisoned not more than 1 year, or both; or (2) in the case of a second or subsequent offense under this section, shall be fined under this title, imprisoned for not more than 2 years, or both. (b) Definition In this section: (1) The term protected adult means an individual who is 18 years of age or older and who is unable to protect themselves from abuse, neglect, or exploitation at the time of offense, due to one or more of the following: (A) Autism spectrum disorder (as such term is defined in the most recent edition of the Diagnostic and Statistical Manual of Mental Disorders, as of the date of the commission of the offense). (B) Intellectual developmental disorder (as such term is defined in the most recent edition of the Diagnostic and Statistical Manual of Mental Disorders, as of the date of the commission of the offense) or an intellectual disability (as such term is defined in the edition of the International Classification of Diseases most recently adopted by the Department of Health and Human Services, as of the date of the commission of the offense). (C) Cerebral palsy (as such term is defined in the edition of the International Classification of Diseases most recently adopted by the Department of Health and Human Services, as of the date of the commission of the offense). (D) Down syndrome (as such term is defined in the edition of the International Classification of Diseases most recently adopted by the Department of Health and Human Services, as of the date of the commission of the offense). (E) Major neurocognitive disorder (as such term is defined in the most recent edition of the Diagnostic and Statistical Manual of Mental Disorders, as of the date of the commission of the offense). (F) Dementia or Alzheimer\u2019s disease (as such terms are defined in the edition of the International Classification of Diseases most recently adopted by the Department of Health and Human Services, as of the date of the commission of the offense). (G) Schizophrenia or another psychotic disorder (as such term is defined in the most recent edition of the Diagnostic and Statistical Manual of Mental Disorders, as of the date of the commission of the offense). (2) The term harm means any harm, whether physical, psychological, financial, or reputational harm. .\n##### (b) Clerical amendment\nThe table of sections for chapter 109A of title 18, United States Code, is amended by inserting after the item related to section 2245 the following:\n2245A. Sexual exploitation of protected adults. .",
      "versionDate": "2026-02-25",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-27T20:03:15Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7715ih.xml"
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
      "title": "Justice for Allie Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for Allie Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit coercing protected adults to send or otherwise transmit an intimate visual depiction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:25Z"
    }
  ]
}
```
