# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3813
- Title: CLEAR Act
- Congress: 119
- Bill type: S
- Bill number: 3813
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-02-27T19:56:01Z
- Update date including text: 2026-02-27T19:56:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3813",
    "number": "3813",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CLEAR Act",
    "type": "S",
    "updateDate": "2026-02-27T19:56:01Z",
    "updateDateIncludingText": "2026-02-27T19:56:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T16:45:20Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3813is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3813\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Schiff (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require a notice be submitted to the Register of Copyrights with respect to copyrighted works used in building generative artificial intelligence models, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Copyright Labeling and Ethical AI Reporting Act or the CLEAR Act .\n#### 2. Notice to be submitted to the Register of Copyrights with respect to copyrighted works used in building generative AI models\n##### (a) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence means an automated system designed to perform a task typically associated with human intelligence or cognitive function.\n**(2) Copyrighted work**\nThe term copyrighted work means a work that is\u2014\n**(A)**\nprotected under title 17, United States Code; and\n**(B)**\nregistered under section 408, or scheduled pursuant to section 1401, of title 17, United States Code.\n**(3) Generative AI model**\nThe term generative AI model means a combination of computer code and numerical values that is designed to use artificial intelligence to generate outputs in the form of expressive material, such as text, images, audio, or video.\n**(4) Register**\nThe term Register means the Register of Copyrights.\n**(5) Training dataset**\nThe term training dataset means a collection of individual units of material, including any combination of text, images, audio, video, or other categories of material, and annotations, if any, describing that material.\n##### (b) Notice\n**(1) Requirement**\nA person that uses a training dataset in connection with the training or release of a generative AI model shall submit to the Register notice that contains\u2014\n**(A)**\na sufficiently detailed summary of each copyrighted work in the training dataset; and\n**(B)**\nthe Uniform Resource Locator for that training dataset, if the training dataset is publicly available on the internet at the time the person submits the notice.\n**(2) Time for filing notice**\nThe notice required under paragraph (1) shall be submitted\u2014\n**(A)**\nnot later than 30 days before the date on which the applicable generative AI model is used commercially (including when that use is internal to an organization) or released (without regard to whether that release is commercial in nature or whether that release is to the public or to a third party), in the case that the generative AI model is first used or released on or after the effective date of this Act; and\n**(B)**\nnot later than 30 days after the date on which the Register issues regulations under paragraph (3), in the case that the applicable generative AI model is first used or released before the effective date of this Act.\n**(3) Regulations**\nNot later than 180 days after the effective date of this Act, the Register shall issue regulations establishing the form, content, and filing procedures for the notice required under this subsection.\n##### (c) Enforcement\n**(1) Cause of action**\nIf a person uses a copyrighted work in a manner described in subsection (b) without submitting the notice required under that subsection, the owner of the copyrighted work may bring an action in an appropriate district court of the United States against that person.\n**(2) Penalties**\nSubject to paragraph (3), in an action brought under paragraph (1), the court may\u2014\n**(A)**\nimpose a civil penalty, to be paid by the person against which the action is brought\u2014\n**(i)**\nin an amount that is not less than $5,000 for each instance in which the person against which the action is brought failed to submit the required notice; and\n**(ii)**\nwhich shall be paid to the Register, who shall use the penalty amount to offset the operating costs of the Copyright Office;\n**(B)**\nissue an injunction that requires the person against which the action is brought to stop using the applicable work in the manner described in subsection (b) until that person submits the notice required under that subsection; and\n**(C)**\naward to the owner of the applicable copyrighted work attorney\u2019s fees and expenses with respect to the action.\n**(3) Limitation**\n**(A) In general**\nIn any year, a person may not be subject to more than $2,500,000 in total civil penalties imposed under paragraph (2)(A).\n**(B) Other penalties remain available**\nThe limitation under subparagraph (A) shall not affect the ability of the owner of a copyrighted work, during the period in which that limitation applies, to obtain a remedy described in subparagraph (B) or (C) of paragraph (2) with respect to an action brought by the owner under paragraph (1).\n##### (d) Database\nThe Register shall establish and maintain a publicly available online database that contains each notice submitted under subsection (b)(1).\n##### (e) Effective date\nThis Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-02-10",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-02-27T19:56:00Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3813is.xml"
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
      "title": "CLEAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Copyright Labeling and Ethical AI Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a notice be submitted to the Register of Copyrights with respect to copyrighted works used in building generative artificial intelligence models, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T03:48:25Z"
    }
  ]
}
```
