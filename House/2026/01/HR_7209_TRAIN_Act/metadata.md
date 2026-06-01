# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7209?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7209
- Title: TRAIN Act
- Congress: 119
- Bill type: HR
- Bill number: 7209
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-03-25T08:06:01Z
- Update date including text: 2026-03-25T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7209",
    "number": "7209",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "TRAIN Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:01Z",
    "updateDateIncludingText": "2026-03-25T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:00:25Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7209ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7209\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Dean of Pennsylvania (for herself and Mr. Moran ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo create an administrative subpoena process to assist copyright owners in determining which of their copyrighted works have been used in the training of artificial intelligence models.\n#### 1. Short title\nThis Act may be cited as the Transparency and Responsibility for Artificial Intelligence Networks Act or the TRAIN Act .\n#### 2. Subpoena for copies or records relating to artificial intelligence models\n##### (a) In general\nChapter 5 of title 17, United States Code, is amended by adding at the end the following:\n514. Subpoena for copies or records relating to artificial intelligence models (a) Definitions In this section: (1) Artificial intelligence The term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ). (2) Artificial intelligence model The term artificial intelligence model means a component of an information system that implements artificial intelligence technology and uses computational, statistical, or machine-learning techniques to produce outputs from a given set of inputs. (3) Developer The term developer \u2014 (A) means a person or State or local government agency that\u2014 (i) designs, codes, produces, owns, or substantially modifies a generative artificial intelligence model for use by\u2014 (I) the person or State or local government agency; or (II) a third party; and (ii) engages in or supervises, including as a third party training dataset curator\u2014 (I) the curation of the training dataset of the artificial intelligence model; or (II) the use of the training dataset to train the artificial intelligence model; and (B) does not include a noncommercial end user of a generative artificial intelligence model. (4) Generative artificial intelligence model The term generative artificial intelligence model \u2014 (A) means an artificial intelligence model that emulates the structure and characteristics of input data in order to generate derived synthetic content, which may include images, videos, audio, text, and other digital content; and (B) includes any subsequent variation on an artificial intelligence model described in subparagraph (A), even if created by a third party. (5) Substantially modify The term substantially modify , with respect to a generative artificial intelligence model, means to take 1 or more actions leading to a new version of, new release of, or other update to the generative artificial intelligence model that materially changes the functionality or performance of the generative artificial intelligence model, including by retraining or fine tuning the generative artificial intelligence model. (6) Training material The term training material means individual works or components thereof used for the purpose of training a generative artificial intelligence model, including a combination of text, images, audio, or other categories of expressive materials, as well as annotations describing the material. (b) Request (1) In general The legal or beneficial owner of an exclusive right under a copyright, or a person authorized to act on the owner's behalf, may request the clerk of any United States district court to issue a subpoena to a developer for disclosure of copies of, or records sufficient to identify with certainty, the copyrighted works, or any portion thereof, likely owned or controlled by the legal or beneficial owner that were used by the developer to train the generative artificial intelligence model, if the legal or beneficial owner or authorized person has a subjective good faith belief that the developer used some or all of 1 or more such copyrighted works to train the generative artificial intelligence model. (2) Subpoena limited to requester's own copyrighted work Nothing in paragraph (1) shall be construed to authorize a legal or beneficial owner of an exclusive right under a copyright, or a person authorized to act on the owner's behalf, to request a subpoena for disclosure of copies of, or records sufficient to identify with certainty, copyrighted works likely owned or controlled by any person other than the legal or beneficial owner. (c) Contents of request A request under subsection (b) may be made by filing with the clerk\u2014 (1) a proposed subpoena; and (2) a sworn declaration to the effect that\u2014 (A) the legal or beneficial owner or authorized person has a subjective good faith belief that the developer used some or all of 1 or more of the copyrighted works owned or controlled by the legal or beneficial owner to train the generative artificial intelligence model; (B) the purpose for which the subpoena is sought is to obtain copies of the training material, or records sufficient to identify with certainty the training material, used to train the generative artificial intelligence model in order to determine whether the developer has used copyrighted works owned or controlled by the legal or beneficial owner in connection with the generative artificial intelligence model; and (C) the copies or records will only be used for the purpose of protecting the rights of the legal or beneficial owner. (d) Contents of subpoena A subpoena issued pursuant to a request under subsection (b) shall authorize and order the developer receiving the subpoena to expeditiously disclose to the legal or beneficial owner or authorized person all records described in that subsection. (e) Basis for granting subpoena If a proposed subpoena described in subsection (c)(1) is in proper form, and the accompanying declaration described in subsection (c)(2) is properly executed, the clerk shall expeditiously issue and sign the proposed subpoena and return it to the requester for delivery to the developer. (f) Actions of developer receiving subpoena Upon receipt of a subpoena issued under subsection (e), a developer shall expeditiously disclose to the legal or beneficial owner or authorized person the copies or records requested by the subpoena. (g) Duty of confidentiality A legal or beneficial owner or authorized person who receives copies or records from a developer under this section may not disclose the copies or records to any other person without proper authorization or consent. (h) Rules applicable to subpoena Unless otherwise provided by this section or by applicable rules of the court, the procedure for issuance and delivery of a subpoena issued under subsection (e), and the remedies for noncompliance with the subpoena, shall be governed to the greatest extent practicable by the provisions of the Federal Rules of Civil Procedure governing the issuance, service, and enforcement of a subpoena duces tecum. (i) Rebuttable presumption If a developer fails to comply with a subpoena issued under subsection (e), that failure shall provide a rebuttable presumption that the developer made copies of the copyrighted work. (j) Sanctions for bad faith subpoena request (1) Motion If the legal or beneficial owner of an exclusive right under a copyright, or a person authorized to act on the owner\u2019s behalf, requests a subpoena under subsection (b) in bad faith, the court that issued the subpoena, upon motion of the recipient of the subpoena, may impose sanctions on the legal or beneficial owner or authorized person. (2) Implementation Rule 11(c) of the Federal Rules of Civil Procedure shall apply to sanctions imposed under this subsection in the same manner as that rule applies to sanctions imposed for a violation of rule 11(b) of those Rules. (k) Effective date This section shall take effect on the date of enactment of this section. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 5 of title 17, United States Code, is amended by adding at the end the following:\n514. Subpoena for copies or records relating to artificial intelligence models. .",
      "versionDate": "2026-01-22",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2455",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TRAIN Act",
      "type": "S"
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
        "updateDate": "2026-01-26T15:08:21Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7209ih.xml"
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
      "title": "TRAIN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRAIN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency and Responsibility for Artificial Intelligence Networks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To create an administrative subpoena process to assist copyright owners in determining which of their copyrighted works have been used in the training of artificial intelligence models.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T09:18:21Z"
    }
  ]
}
```
