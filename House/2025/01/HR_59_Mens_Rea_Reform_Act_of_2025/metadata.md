# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/59?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/59
- Title: Mens Rea Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 59
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-05-27T14:20:28Z
- Update date including text: 2026-05-27T14:20:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-06-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-10 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 13.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-06-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-10 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/59",
    "number": "59",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Mens Rea Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T14:20:28Z",
    "updateDateIncludingText": "2026-05-27T14:20:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
        "item": [
          {
            "date": "2025-06-10T21:28:56Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-03T16:07:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr59ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 59\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Ogles ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo specify the state of mind required for conviction for criminal offenses that lack an expressly identified state of mind, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mens Rea Reform Act of 2025 .\n#### 2. State of mind element for criminal offenses\n##### (a) In general\nChapter 1 of title 18, United States Code, is amended by adding at the end the following:\n28. State of mind when not otherwise specifically provided (a) Definitions In this section\u2014 (1) the term covered offense \u2014 (A) means an offense\u2014 (i) specified in\u2014 (I) this title or any other Act of Congress; (II) any regulation; or (III) any law (including regulations) of any State or foreign government incorporated by reference into this title or any other Act of Congress; and (ii) that is punishable by imprisonment, a maximum criminal fine of at least $2,500, or both; and (B) does not include\u2014 (i) any offense set forth in chapter 47 or chapter 47A of title 10; or (ii) any offense incorporated by section 13(a) of this title; (2) the term knowingly , as related to an element of an offense, means\u2014 (A) if the element involves the nature of the conduct of a person or the attendant circumstances, that the person is aware that the conduct of the person is of that nature or that such circumstances exist; and (B) if the element involves a result of the conduct of a person, that the person is aware that it is practically certain that the conduct of the person will cause such a result; (3) the term state of mind means willfully, intentionally, maliciously, knowingly, recklessly, wantonly, negligently, with reason to believe, or any other word or phrase that is synonymous with or substantially similar to any such term; and (4) the term willfully , as related to an element of an offense, means\u2014 (A) that the person acted with knowledge that the person\u2019s conduct was unlawful; and (B) if the element involves the nature, attendant circumstances, object, or result of the conduct of a person, that\u2014 (i) the person had knowledge of the nature, attendant circumstances, object, or result of the conduct of the person; and (ii) it was the conscious object of the person to engage in conduct\u2014 (I) of that nature; (II) with that attendant circumstance; (III) with that object; or (IV) to cause such a result. (b) Default requirement Except as provided in subsections (c) and (d), a covered offense shall be construed to require the Government to prove beyond a reasonable doubt that the defendant acted\u2014 (1) with the state of mind specified in the text of the covered offense for each element of the offense for which the text specifies a state of mind; and (2) knowingly, with respect to any element of the offense for which the text of the covered offense does not specify a state of mind. (c) Failure To distinguish among elements Except as provided in subsection (d), if the text of a covered offense specifies the state of mind required for commission of the covered offense without specifying the elements of the covered offense to which the state of mind applies, the state of mind specified shall apply to all elements of the covered offense, unless a contrary purpose plainly appears. (d) Exceptions (1) In general Subsections (b)(2) and (c) shall not apply with respect to\u2014 (A) any element for which the text of the covered offense makes clear that Congress affirmatively intended not to require the Government to prove any state of mind with respect to such element; (B) any element of a covered offense, to the extent that the element establishes\u2014 (i) subject matter jurisdiction over the covered offense; or (ii) venue with respect to trial of the covered offense; or (C) any element of a covered offense, to the extent that applying subsections (b)(2) and (c) to such element would lessen the degree of mental culpability that the Government is required to prove with respect to that element under\u2014 (i) precedent of the Supreme Court of the United States; or (ii) any other provision of this title, any other Act of Congress, or any regulation. (2) Mere absence insufficient For purposes of paragraph (1)(A), the mere absence of a specified state of mind for an element of a covered offense in the text of the covered offense shall not be construed to mean that Congress affirmatively intended not to require the Government to prove any state of mind with respect to that element. (e) Applicability This section shall apply with respect to a covered offense\u2014 (1) without regard to whether the provision or provisions specifying the covered offense are enacted, promulgated, or finalized before, on, or after the date of enactment of this section; and (2) that was committed\u2014 (A) on or after the date of enactment of this section; or (B) before the date of enactment of this section, unless\u2014 (i) applying this section to such covered offense would\u2014 (I) punish as a crime conduct that was innocent when done; (II) increase the punishment for the covered offense; or (III) deprive a person charged with the covered offense of any defense available according to law at the time the covered offense occurred; (ii) a jury has been empaneled and sworn in a prosecution for the covered offense before the date of enactment of this section; (iii) the first witness has been sworn in a prosecution for the covered offense tried without a jury before the date of enactment of this section; or (iv) a sentence has been imposed following a plea of guilty or nolo contendere in a prosecution for the covered offense before the date of enactment of this section. (f) Subsequently enacted laws No provision of law enacted after the date of enactment of this section shall be construed to repeal, modify the text or effect of, or supersede in whole or in part this section, unless such law specifically refers to this section and explicitly repeals, modifies the text or effect of, or supersedes in whole or in part this section. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 1 of title 18, United States Code, is amended by adding at the end the following:\n28. State of mind when not otherwise specifically provided. .",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-26T14:35:18Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-02-26T14:35:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-04T12:09:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr59",
          "measure-number": "59",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr59v00",
            "update-date": "2025-02-11"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mens Rea Reform Act of 2025</strong></p><p>This bill establishes a default <em>mens rea</em> standard (i.e., state of mind requirement) for federal criminal offenses\u2014statutory and regulatory\u2014that lack an explicit standard.</p><p>The government must generally prove that a defendant acted knowingly with respect to each element of an offense for which the text does not specify a state of mind.</p><p>\u00a0</p>"
        },
        "title": "Mens Rea Reform Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr59.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mens Rea Reform Act of 2025</strong></p><p>This bill establishes a default <em>mens rea</em> standard (i.e., state of mind requirement) for federal criminal offenses\u2014statutory and regulatory\u2014that lack an explicit standard.</p><p>The government must generally prove that a defendant acted knowingly with respect to each element of an offense for which the text does not specify a state of mind.</p><p>\u00a0</p>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr59"
    },
    "title": "Mens Rea Reform Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mens Rea Reform Act of 2025</strong></p><p>This bill establishes a default <em>mens rea</em> standard (i.e., state of mind requirement) for federal criminal offenses\u2014statutory and regulatory\u2014that lack an explicit standard.</p><p>The government must generally prove that a defendant acted knowingly with respect to each element of an offense for which the text does not specify a state of mind.</p><p>\u00a0</p>",
      "updateDate": "2025-02-11",
      "versionCode": "id119hr59"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr59ih.xml"
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
      "title": "Mens Rea Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:23:19Z"
    },
    {
      "title": "Mens Rea Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To specify the state of mind required for conviction for criminal offenses that lack an expressly identified state of mind, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:18:14Z"
    }
  ]
}
```
