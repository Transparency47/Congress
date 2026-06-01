# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2620
- Title: REMEDY Act
- Congress: 119
- Bill type: S
- Bill number: 2620
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-18T19:45:41Z
- Update date including text: 2025-09-18T19:45:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S5000: 1)
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S5000: 1)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2620",
    "number": "2620",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "REMEDY Act",
    "type": "S",
    "updateDate": "2025-09-18T19:45:41Z",
    "updateDateIncludingText": "2025-09-18T19:45:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S5000: 1)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T20:08:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2620is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2620\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Durbin (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act with respect to approval of abbreviated new drug applications.\n#### 1. Short title\nThis Act may be cited as the Reforming Evergreening and Manipulation that Extends Drug Years Act or the REMEDY Act .\n#### 2. Amendments to ANDA approval provisions\nSection 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) is amended\u2014\n**(1)**\nin subsection (c)(2) by adding at the end the following: With respect to a drug approved on or after the date of enactment of the Reforming Evergreening and Manipulation that Extends Drug Years Act , when a holder of an approved application first files information under this paragraph with respect to one or more patents described in subsection (b)(1)(A)(viii), the holder shall select one such patent with respect to which the owner or licensee may be eligible for the thirty-month period under paragraph (3)(C) or subsection (j)(5)(B)(iii), as applicable; for purposes of paragraphs (3)(C) and (3)(E)(ii) and subsections (j)(5)(B)(iii) and (j)(5)(F)(ii), such patent shall be referred to as the covered patent . The selection of such covered patent may not be changed or amended. ;\n**(2)**\nin subsection (c)(3)(C)\u2014\n**(A)**\nin the matter preceding clause (i)\u2014\n**(i)**\nby striking an action is brought for infringement and all that follows through the period at the end of the first sentence and inserting with respect to a drug approved under this subsection before the date of enactment of the Reforming Evergreening and Manipulation that Extends Drug Years Act , an action is brought for infringement of any patent that is the subject of the certification and for which information was submitted to the Secretary under paragraph (2) before the date on which the application (excluding an amendment or supplement to the application) was submitted, or, with respect to a drug approved under this subsection on or after the date of enactment of the Reforming Evergreening and Manipulation that Extends Drug Years Act , an action is brought for infringement of the covered patent (as described in paragraph (2)) that is the subject of the certification and for which information was submitted to the Secretary under paragraph (2) before the date on which the application (excluding an amendment or supplement to the application) was submitted. ; and\n**(ii)**\nby striking an action is brought before and inserting an action with respect to a patent or a covered patent, as applicable, is brought before ; and\n**(B)**\nin clause (i), by striking decides that the patent and inserting decides that the patent or the covered patent, as applicable ;\n**(3)**\nin the second sentence of subsection (c)(3)(E)(ii), by inserting with respect to any patent for which the requirements are met for the thirty-month period described in subparagraph (C) after action for patent infringement ;\n**(4)**\nin subsection (j)(5)(B)(iii)\u2014\n**(A)**\nin the matter preceding subclause (I)\u2014\n**(i)**\nby striking an action is brought for infringement and all that follows through the period at the end of the first sentence and inserting with respect to a drug approved under subsection (c) before the date of enactment of the Reforming Evergreening and Manipulation that Extends Drug Years Act , an action is brought for infringement of any patent that is the subject of the certification and for which information was submitted to the Secretary under subsection (c)(2) before the date on which the application (excluding an amendment or supplement to the application), which the Secretary later determines to be substantially complete, was submitted, or, with respect to a drug approved under subsection (c) on or after the date of enactment of the Reforming Evergreening and Manipulation that Extends Drug Years Act , an action is brought for infringement of the covered patent (as described in subsection (c)(2)) that is the subject of the certification and for which information was submitted to the Secretary under subsection (c)(2) before the date on which the application (excluding an amendment or supplement to the application), which the Secretary later determines to be substantially complete, was submitted. ; and\n**(ii)**\nby striking an action is brought before and inserting an action with respect to a patent or a covered patent, as applicable, is brought before ; and\n**(B)**\nin subclause (I), by striking decides that the patent and inserting decides that the patent or covered patent, as applicable, ; and\n**(5)**\nin the second sentence of subsection (j)(5)(F)(ii), by inserting with respect to any patent for which the requirements are met for the thirty-month period described in subparagraph (B)(iii), after action for patent infringement .",
      "versionDate": "2025-07-31",
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
        "name": "Health",
        "updateDate": "2025-09-18T19:45:41Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2620is.xml"
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
      "title": "REMEDY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REMEDY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reforming Evergreening and Manipulation that Extends Drug Years Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act with respect to approval of abbreviated new drug applications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:24Z"
    }
  ]
}
```
