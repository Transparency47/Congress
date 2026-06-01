# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3256
- Title: Disarm Hate Act
- Congress: 119
- Bill type: S
- Bill number: 3256
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3256",
    "number": "3256",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Disarm Hate Act",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
            "date": "2025-11-20T19:11:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T19:11:26Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3256is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3256\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Luj\u00e1n introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prevent a person who has been convicted of a misdemeanor hate crime, or has received an enhanced sentence for a misdemeanor because of hate or bias in its commission, from obtaining a firearm.\n#### 1. Short title\nThis Act may be cited as the Disarm Hate Act .\n#### 2. Prevention of person who has been convicted of a misdemeanor hate crime, or received an enhanced sentence for a misdemeanor because of hate or bias in its commission, from obtaining a firearm\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) The term convicted in any court of a misdemeanor hate crime \u2014 (A) means being convicted by a court of an offense that\u2014 (i) is a misdemeanor under Federal, State, or Tribal law; (ii) has, as an element, that the conduct of the offender was motivated by hate or bias because of the actual or perceived race, color, religion, national origin, gender, sexual orientation, gender identity (as defined in section 249), or disability of any person; and (iii) involves the use or attempted use of physical force, the threatened use of a deadly weapon, or another credible threat to the physical safety of any person; and (B) does not include\u2014 (i) a conviction of an offense described in subparagraph (A), unless\u2014 (I) the person\u2014 (aa) was represented by counsel in the case; or (bb) knowingly and intelligently waived the right to counsel in the case; and (II) in the case of a prosecution for an offense described in subparagraph (A) for which a person was entitled to a jury trial in the jurisdiction in which the case was tried\u2014 (aa) the case was tried by a jury; or (bb) the person knowingly and intelligently waived the right to have the case tried by a jury, by guilty plea or otherwise; or (ii) a conviction of an offense described in subparagraph (A) if\u2014 (I) the conviction\u2014 (aa) has been expunged or set aside; or (bb) is of an offense for which the person has been pardoned or has had civil rights restored (if the law of the applicable jurisdiction provides for the loss of civil rights under such an offense); and (II) the expungement, pardon, or restoration of civil rights does not expressly provide that the person may not ship, transport, possess, or receive firearms. (40) The term received from any court an enhanced hate crime misdemeanor sentence \u2014 (A) means a court has imposed a sentence for a misdemeanor under Federal, State, or Tribal law\u2014 (i) that involves the use or attempted use of physical force, the threatened use of a deadly weapon, or another credible threat to the physical safety of any person; and (ii) based, in whole or in part, on a judicial finding that the conduct of the offender was motivated, in whole or in part, by hate or bias for any reason referred to in paragraph (39)(A)(ii); and (B) does not include\u2014 (i) the imposition of a sentence described in subparagraph (A), unless\u2014 (I) the person\u2014 (aa) was represented by counsel in the case; or (bb) knowingly and intelligently waived the right to counsel in the case; and (II) if the sentence described in subparagraph (A) was imposed in a prosecution for an offense for which a person was entitled to a jury trial in the jurisdiction in which the case was tried\u2014 (aa) the case was tried by a jury; or (bb) the person knowingly and intelligently waived the right to have the case tried by a jury, by guilty plea or otherwise; or (ii) the imposition of a sentence described in subparagraph (A) if\u2014 (I) (aa) the conviction of the offense for which the sentence was imposed has been expunged or set aside; or (bb) the offense for which the sentence was imposed is an offense for which the person has been pardoned or has had civil rights restored (if the law of the applicable jurisdiction provides for the loss of civil rights under such an offense); and (II) the expungement, pardon, or restoration of civil rights does not expressly provide that the person may not ship, transport, possess, or receive firearms. .\n##### (b) Prohibition on sale or other disposition of firearm\nSection 922(d) of title 18, United States Code, is amended, in the first sentence\u2014\n**(1)**\nin paragraph (10), by striking or at the end;\n**(2)**\nby redesignating paragraph (11) as paragraph (12);\n**(3)**\nin paragraph (12), as so redesignated, by striking through (10) and inserting through (11) ; and\n**(4)**\nby inserting after paragraph (10) the following:\n(11) has been convicted in any court of a misdemeanor hate crime, or has received from any court an enhanced hate crime misdemeanor sentence; or .\n##### (c) Prohibition on possession, shipment, or transport of firearm\nSection 922(g) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (8), by striking or at the end;\n**(2)**\nin paragraph (9), by striking the comma and inserting ; or ; and\n**(3)**\nby inserting after paragraph (9) the following:\n(10) who has been convicted in any court of a misdemeanor hate crime, or has received from any court an enhanced hate crime misdemeanor sentence, .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6258",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Disarm Hate Act",
      "type": "HR"
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
        "updateDate": "2025-12-19T16:42:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119s3256",
          "measure-number": "3256",
          "measure-type": "s",
          "orig-publish-date": "2025-11-20",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3256v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Disarm Hate Act</strong></p><p>This bill expands the categories of persons who are prohibited from receiving or possessing a firearm.</p><p>Specifically, it prohibits firearm sale or transfer to and receipt, possession, shipment, or transport by a person (1) who has been convicted of a misdemeanor hate crime, or (2) who has received an enhanced hate crime misdemeanor sentence.</p>"
        },
        "title": "Disarm Hate Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3256.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disarm Hate Act</strong></p><p>This bill expands the categories of persons who are prohibited from receiving or possessing a firearm.</p><p>Specifically, it prohibits firearm sale or transfer to and receipt, possession, shipment, or transport by a person (1) who has been convicted of a misdemeanor hate crime, or (2) who has received an enhanced hate crime misdemeanor sentence.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s3256"
    },
    "title": "Disarm Hate Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disarm Hate Act</strong></p><p>This bill expands the categories of persons who are prohibited from receiving or possessing a firearm.</p><p>Specifically, it prohibits firearm sale or transfer to and receipt, possession, shipment, or transport by a person (1) who has been convicted of a misdemeanor hate crime, or (2) who has received an enhanced hate crime misdemeanor sentence.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s3256"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3256is.xml"
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
      "title": "Disarm Hate Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disarm Hate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent a person who has been convicted of a misdemeanor hate crime, or has received an enhanced sentence for a misdemeanor because of hate or bias in its commission, from obtaining a firearm.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T06:33:37Z"
    }
  ]
}
```
