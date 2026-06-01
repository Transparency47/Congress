# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3808?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3808
- Title: Fighting Trade Cheats Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3808
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-02-27T15:56:53Z
- Update date including text: 2026-02-27T15:56:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3808",
    "number": "3808",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Fighting Trade Cheats Act of 2026",
    "type": "S",
    "updateDate": "2026-02-27T15:56:53Z",
    "updateDateIncludingText": "2026-02-27T15:56:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T22:05:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3808is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3808\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mrs. Britt (for herself, Ms. Baldwin , Mr. Tillis , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Tariff Act of 1930 to increase civil penalties for, and improve enforcement with respect to, customs fraud, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Trade Cheats Act of 2026 .\n#### 2. Increase in civil penalties for fraudulent and grossly negligent violations of United States customs laws\nSection 592 of the Tariff Act of 1930 ( 19 U.S.C. 1592 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraph (2) as paragraph (3); and\n**(B)**\nby inserting after paragraph (1) the following:\n(2) Presumption (A) In general For purposes of paragraph (1)(B), if a person purchases merchandise from two or more affiliated persons after such persons are determined by U.S. Customs and Border Protection or a court of competent jurisdiction to have violated subsection (a) by means of fraud or gross negligence, there shall be a presumption that the purchaser had knowledge of such violation with respect to purchases from the second or subsequent such affiliated person. (B) Affiliated person defined In subparagraph (A), the term affiliated person has the meaning given that term in section 771(33). ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking A fraudulent violation and inserting the following:\n(A) In general A fraudulent violation ;\n**(ii)**\nin subparagraph (A) (as so designated), by inserting before the domestic value the following: three times ; and\n**(iii)**\nby adding at the end the following:\n(B) Additional penalties A person\u2014 (i) that commits a fraudulent violation of subsection (a) shall be prohibited from importing merchandise into the United States during a period of five years beginning on the date of entry of a final judgment with respect to such violation; and (ii) that is an affiliated person of a person described in clause (i) shall be prohibited from importing merchandise into the United States during the period described in such clause. (C) Affiliated person defined In subparagraph (B)(ii), the term affiliated person has the meaning given that term in section 771(33). ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking A grossly negligent violation and inserting the following:\n(A) In general A grossly negligent violation ;\n**(ii)**\nby striking (A) the lesser of\u2014 and inserting the following:\n(i) the lesser of\u2014 ;\n**(iii)**\nby striking (i) the domestic value and inserting the following:\n(I) three times the domestic value ;\n**(iv)**\nby striking (ii) four times and inserting the following:\n(II) 10 times ;\n**(v)**\nby striking (B) if the violation and inserting the following:\n(ii) if the violation ;\n**(vi)**\nin clause (ii) of subparagraph (A) (as so redesignated), by striking 40 percent of and inserting three times ; and\n**(vii)**\nby adding at the end the following:\n(B) Additional penalties A person\u2014 (i) that commits a grossly negligent violation of subsection (a) shall be prohibited from importing merchandise into the United States during a period of two years beginning on the date of entry of a final judgment with respect to such violation; and (ii) that is an affiliated person of a person described in clause (i) shall be prohibited from importing merchandise into the United States during the period described in such clause. (C) Affiliated person defined In subparagraph (B)(ii), the term affiliated person has the meaning given that term in section 771(33). .\n#### 3. Private enforcement action for customs fraud\nThe Tariff Act of 1930 is amended by inserting after section 592A ( 19 U.S.C. 1592a ) the following:\n592B. Private enforcement action for customs fraud (a) Civil action An interested party the business, property, or other financial interest of which is injured by a fraudulent or grossly negligent violation of section 592(a) may bring a civil action against any person that causes such injury, or any person that aids or abets that person in violating section 592(a), in any United States District Court located in a district in which the interested party has suffered injury, without regard to the amount in controversy. (b) Relief Upon proof by an interested party in a civil action brought under subsection (a) that the business, property, or other financial interest of the interested party has been injured by a fraudulent or grossly negligent violation of section 592(a), the interested party shall\u2014 (1) (A) recover compensatory damages equal to the amount of such injury plus an additional penalty equal to three times the amount of compensatory damages; and (B) be granted such equitable relief as may be appropriate, which may include an injunction against further importation into the United States of the merchandise imported into the United States in violation of section 592(a); and (2) recover the costs of bringing the civil action, including reasonable attorney\u2019s fees. (c) Intervention by the United States (1) In general The court shall permit the United States to intervene in an civil action brought under subsection (a), as a matter of right. The United States shall have all the rights of a party. (2) Sharing of information Upon a reasonable request by the United States Government, any interested party that brings a civil action under subsection (a) shall provide to the United States Government\u2014 (A) a copy of the complaint; (B) any memoranda of law or briefing filed with a court in support of the complaint as of the date of the request; and (C) if the United States Government agrees to reimburse the interested party for all reasonable costs and expenses associated with responding to the request, any information obtained by the interested party through discovery processes in the civil action as of the date of the request. (d) Interested party defined (1) In general In this section, the term interested party means\u2014 (A) a manufacturer, producer, or wholesaler in the United States of like merchandise or competing merchandise; (B) a certified union or recognized union or group of workers that is representative of an industry engaged in the manufacture, production, or wholesale in the United States of like merchandise or competing merchandise; or (C) a trade or business association a majority of the members of which manufacture, produce, or wholesale like merchandise or competing merchandise in the United States. (2) Competing merchandise For purposes of paragraph (1), the term competing merchandise means merchandise that competes with or is a substitute for merchandise being imported into the United States in violation of section 592(a). (3) Like merchandise For purposes of paragraph (1), the term like merchandise means merchandise that is like, or in the absence of like, most similar in characteristics and uses with, merchandise being imported into the United States in violation of section 592(a). .\n#### 4. Exclusion of persons that have committed fraudulent or grossly negligent violations of United States customs laws from participation in the importer of record program\nSection 114 of the Trade Facilitation and Trade Enforcement Act of 2015 ( 19 U.S.C. 4320 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Exclusion (1) In general The following persons shall be ineligible to participate in the importer of record program: (A) Any person determined by U.S. Customs and Border Protection or a court of competent jurisdiction to have committed a fraudulent or grossly negligent violation of section 592(a) of the Tariff Act of 1930 ( 19 U.S.C. 1592(a) ). (B) Any person that is an affiliated person of a person described in subparagraph (A). (2) Revocation The Secretary shall revoke the importer of record number assigned to any person under the importer of record program if the Secretary subsequently determines that the person is a person described in subparagraph (A) or (B) of paragraph (1). (3) Affiliated person defined (A) In general For purposes paragraph (1)(B), the term affiliated person has the meaning given that term in section 771(33) of the Tariff Act of 1930 ( 19 U.S.C. 1677(33) ). (B) Deemed affiliated persons In order to prevent commercial fraud, protect the revenue, and help prevent the use of shell companies by importers that seek to evade the customs and trade laws of the United States, a person may be deemed to be an affiliated person for purposes of paragraph (1)(B) based upon information declared to U.S. Customs and Border Protection suggesting a formal or ongoing relationship between that person and a person described in paragraph (1)(A), including similarities in imported merchandise (including article classification upon importation), common declared exporters and shippers, and historical import volumes. .",
      "versionDate": "2026-02-09",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1284",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fighting Trade Cheats Act of 2025",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-02-25T18:36:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-09",
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
          "measure-id": "id119s3808",
          "measure-number": "3808",
          "measure-type": "s",
          "orig-publish-date": "2026-02-09",
          "originChamber": "SENATE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3808v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2026-02-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fighting Trade Cheats Act of 2026</strong></p><p>This bill increases penalties for, and establishes additional enforcement mechanisms related to, fraudulent and grossly negligent violations of U.S. customs laws.</p><p>Specifically, the bill increases the maximum civil penalty for a fraudulent violation to three times the domestic value of the merchandise. (Currently, the maximum penalty is the domestic value of the merchandise.) It prohibits a person who commits a fraudulent violation from importing merchandise into the United States for a five-year period.</p><p>Additionally, the bill increases the maximum civil penalty for a grossly negligent violation to the lesser of (1) 3 times the domestic value of the merchandise; or (2) 10 times the lawful duties, taxes, and fees. (Currently, the maximum penalty is the lesser of the domestic value of the merchandise or four times the lawful duties, taxes, and fees.) It prohibits a person who commits a grossly negligent violation from importing merchandise into the United States for a two-year period.</p><p>Further, the bill applies these importation bans to an affiliated person (e.g., a family member or employee) of the person who committed the fraudulent or grossly negligent violation.</p><p>The bill establishes a private right of action for an interested party (e.g., a manufacturer) affected by customs fraud or grossly negligent violations.</p><p>The bill prohibits any person (or an affiliated person) who commits a fraudulent or grossly negligent violation from participating in the U.S. Customs and Border Protection's Importer of Record program, and further requires revocation of their importer of record numbers.</p>"
        },
        "title": "Fighting Trade Cheats Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3808.xml",
    "summary": {
      "actionDate": "2026-02-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fighting Trade Cheats Act of 2026</strong></p><p>This bill increases penalties for, and establishes additional enforcement mechanisms related to, fraudulent and grossly negligent violations of U.S. customs laws.</p><p>Specifically, the bill increases the maximum civil penalty for a fraudulent violation to three times the domestic value of the merchandise. (Currently, the maximum penalty is the domestic value of the merchandise.) It prohibits a person who commits a fraudulent violation from importing merchandise into the United States for a five-year period.</p><p>Additionally, the bill increases the maximum civil penalty for a grossly negligent violation to the lesser of (1) 3 times the domestic value of the merchandise; or (2) 10 times the lawful duties, taxes, and fees. (Currently, the maximum penalty is the lesser of the domestic value of the merchandise or four times the lawful duties, taxes, and fees.) It prohibits a person who commits a grossly negligent violation from importing merchandise into the United States for a two-year period.</p><p>Further, the bill applies these importation bans to an affiliated person (e.g., a family member or employee) of the person who committed the fraudulent or grossly negligent violation.</p><p>The bill establishes a private right of action for an interested party (e.g., a manufacturer) affected by customs fraud or grossly negligent violations.</p><p>The bill prohibits any person (or an affiliated person) who commits a fraudulent or grossly negligent violation from participating in the U.S. Customs and Border Protection's Importer of Record program, and further requires revocation of their importer of record numbers.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s3808"
    },
    "title": "Fighting Trade Cheats Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fighting Trade Cheats Act of 2026</strong></p><p>This bill increases penalties for, and establishes additional enforcement mechanisms related to, fraudulent and grossly negligent violations of U.S. customs laws.</p><p>Specifically, the bill increases the maximum civil penalty for a fraudulent violation to three times the domestic value of the merchandise. (Currently, the maximum penalty is the domestic value of the merchandise.) It prohibits a person who commits a fraudulent violation from importing merchandise into the United States for a five-year period.</p><p>Additionally, the bill increases the maximum civil penalty for a grossly negligent violation to the lesser of (1) 3 times the domestic value of the merchandise; or (2) 10 times the lawful duties, taxes, and fees. (Currently, the maximum penalty is the lesser of the domestic value of the merchandise or four times the lawful duties, taxes, and fees.) It prohibits a person who commits a grossly negligent violation from importing merchandise into the United States for a two-year period.</p><p>Further, the bill applies these importation bans to an affiliated person (e.g., a family member or employee) of the person who committed the fraudulent or grossly negligent violation.</p><p>The bill establishes a private right of action for an interested party (e.g., a manufacturer) affected by customs fraud or grossly negligent violations.</p><p>The bill prohibits any person (or an affiliated person) who commits a fraudulent or grossly negligent violation from participating in the U.S. Customs and Border Protection's Importer of Record program, and further requires revocation of their importer of record numbers.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s3808"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3808is.xml"
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
      "title": "Fighting Trade Cheats Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fighting Trade Cheats Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Tariff Act of 1930 to increase civil penalties for, and improve enforcement with respect to, customs fraud, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:27Z"
    }
  ]
}
```
