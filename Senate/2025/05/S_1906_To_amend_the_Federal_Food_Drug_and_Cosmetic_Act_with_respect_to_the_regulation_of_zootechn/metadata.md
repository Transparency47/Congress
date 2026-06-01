# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1906
- Title: Innovative FEED Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1906
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-08T15:24:02Z
- Update date including text: 2026-04-08T15:24:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1906",
    "number": "1906",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Innovative FEED Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T15:24:02Z",
    "updateDateIncludingText": "2026-04-08T15:24:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:39:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "KS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "IA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-22",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MN"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1906is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1906\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Marshall (for himself, Ms. Baldwin , Mr. Moran , Mr. Bennet , Mr. Grassley , Mr. King , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act with respect to the regulation of zootechnical animal food substances.\n#### 1. Short title\nThis Act may be cited as the Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025 .\n#### 2. Regulation of zootechnical animal food substances\n##### (a) Definition\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(tt) (1) The term zootechnical animal food substance means a substance that\u2014 (A) is added to the food or drinking water of animals; (B) is intended to\u2014 (i) affect the byproducts of the digestive process of an animal; (ii) reduce the presence of foodborne pathogens of human health significance in an animal intended to be used for food; or (iii) affect the structure or function of the body of the animal, other than by providing nutritive value, by altering the animal\u2019s gastrointestinal microbiome; and (C) achieves its intended effect by acting solely within the gastrointestinal tract of the animal. (2) Such term does not include a substance that\u2014 (A) is intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in an animal; (B) is a hormone; (C) is an active moiety in an animal drug, which, prior to the filing of a petition under section 409, was approved under section 512, conditionally approved under section 571, indexed under section 572, or for which substantial clinical investigations have been instituted and for which the existence of such investigations has been made public; (D) is an ionophore; or (E) is otherwise excluded from the definition based on criteria established by the Secretary through notice and comment rulemaking. (3) A zootechnical animal food substance shall be deemed to be a food additive within the meaning of paragraph (s) and its introduction into interstate commerce shall be in accordance with a regulation issued under section 409. A zootechnical animal food substance shall not be considered a drug under paragraph (g)(1)(C) solely because the substance has an intended effect described in subparagraph (1). .\n##### (b) Food additives\nSection 409 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 348 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (3) through (5) as paragraphs (4) through (6), respectively; and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) In the case of a zootechnical animal food substance, such petition shall, in addition to any explanatory or supporting data, contain\u2014 (A) all relevant data bearing on the effect the zootechnical animal food substance is intended to have and the quantity of such substance required to produce the intended effect; and (B) full reports of investigations made with respect to the intended use of such substance, including full information as to the methods and controls used in conducting such investigations. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby amending subparagraph (A) of paragraph (1) to read as follows:\n(A) (i) by order establish a regulation (whether or not in accord with that proposed by the petitioner) prescribing\u2014 (I) with respect to one or more proposed uses of the food additive involved, the conditions under which such additive may be safely used (including specifications as to the particular food or classes of food in or on which such additive may be used, the maximum quantity which may be used or permitted to remain in or on such food, the manner in which such additive may be added to or used in or on such food, and any directions or other labeling or packaging requirements for such additive as the Secretary determines necessary to assure the safety of such use); and (II) in the case of a zootechnical animal food substance, the conditions under which such substance may be used to achieve the intended effect; and (ii) notify the petitioner of such order and the reasons for such action; or ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (B), by striking the period and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) in the case of a zootechnical animal food substance, fails to establish that the proposed use of the substance, under the conditions of use to be specified in the regulation, will achieve the intended effect. ; and\n**(3)**\nby adding at the end the following:\n(l) Zootechnical animal food substances The labeling of a zootechnical animal food substance\u2014 (1) shall include the statement: Not for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in animals. ; and (2) may include statements regarding the intended effect of the substance on the structure or function of the body of animals, as set forth in section 201(tt)(1). .\n##### (c) Misbranded food\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If it is a zootechnical animal food substance and the labeling of the food does not include the statement required by section 409(l)(1). .\n##### (d) Rule of construction\nNothing in this section, or the amendments made by this section, shall be construed to authorize the Secretary of Health and Human Services to require the use of any zootechnical food substance or food additive (as those terms are defined in section 201 of the Federal Food, Drug, and Cosmetic Act, as amended by subsection (a)).",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2203",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Innovative FEED Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-06-24T13:52:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
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
          "measure-id": "id119s1906",
          "measure-number": "1906",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1906v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p>"
        },
        "title": "Innovative FEED Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1906.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s1906"
    },
    "title": "Innovative FEED Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s1906"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1906is.xml"
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
      "title": "Innovative FEED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Innovative FEED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Innovative Feed Enhancement and Economic Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act with respect to the regulation of zootechnical animal food substances.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:18Z"
    }
  ]
}
```
