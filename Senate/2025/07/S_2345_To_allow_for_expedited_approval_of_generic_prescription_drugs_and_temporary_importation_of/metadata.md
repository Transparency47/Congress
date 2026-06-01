# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2345
- Title: Short on Competition Act
- Congress: 119
- Bill type: S
- Bill number: 2345
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-24T16:38:14Z
- Update date including text: 2026-04-24T16:38:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2345",
    "number": "2345",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Short on Competition Act",
    "type": "S",
    "updateDate": "2026-04-24T16:38:14Z",
    "updateDateIncludingText": "2026-04-24T16:38:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T19:45:46Z",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "UT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2345is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2345\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Ms. Klobuchar (for herself, Mr. Lee , Mr. Durbin , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo allow for expedited approval of generic prescription drugs and temporary importation of prescription drugs in the case of marginally competitive drug markets and drug shortages.\n#### 1. Short title\nThis Act may be cited as the Short on Competition Act .\n#### 2. Temporary importation of prescription drugs\n##### (a) Temporary importation\nSection 506C of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c ) is amended\u2014\n**(1)**\nby redesignating subsections (h), (i), and (j) as subsections (i), (j), and (k) respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Temporary importation authority (1) In general If, based on notifications described in subsection (a) or any other relevant information, the Secretary concludes that there is, or is likely to be, a drug shortage of a drug described in subsection (a), except as provided in paragraph (3), the Secretary shall authorize importation of such drug for a period of up to 3 years if\u2014 (A) the drug is a drug subject to section 503(b)(1), including a combination product whose primary mode of action is that of a drug as determined under section 503(g)(1)(D)(i), other than a drug described in subparagraphs (A) through (F) of section 804(a)(3); (B) the drug is authorized to be lawfully marketed in one or more of the countries included in the list under section 802(b)(1); (C) the imported drug has the same active ingredient as the drug for which there is a shortage with respect to manufacturers in the United States; (D) the manufacturer certifies to the Secretary that it intends to seek approval of the drug under section 505(j); and (E) an importer (as defined in section 804(a)) files with the Secretary information\u2014 (i) attesting that the requirements under subparagraphs (A) through (D) are satisfied; (ii) identifying the drug the importer proposes to import and the manufacturer from whom the importer proposes to import such drug; and (iii) requesting authority to import the drug. (2) Beginning date of importation Except as provided in paragraph (3), if all of the conditions under paragraph (1) are met, the Secretary shall authorize importation of a drug in accordance with such paragraph beginning not later than 60 days after receipt of the information under paragraph (1)(E). (3) Discretionary denial of importation The Secretary may deny importation of a drug otherwise qualified for importation under paragraph (1) if the Secretary determines that\u2014 (A) the drug is not safe and effective; (B) the drug is used in conjunction with a device for which there is no reasonable assurance of safety and effectiveness; or (C) the authorization to market the drug in one or more of the countries included in the list under section 802(b)(1) has been rescinded or withdrawn because of any concern relating to the safety or effectiveness of the drug. (4) Termination of authority The authority to import a drug pursuant to paragraph (1) shall terminate after 3 years, or when the drug shortage no longer applies, whichever occurs first. .\n##### (b) Marginally competitive drug markets\nChapter V of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 et seq. ) is amended by inserting after section 506C\u20131 the following:\n506C\u20132. Marginally competitive drug markets (a) In general If the Secretary determines under subsection (b) that a marginally competitive market exists with respect to an applicable drug, the Secretary\u2014 (1) shall treat such marginally competitive market as creating a drug shortage only for purposes of subsections (g) and (h) of section 506C; and (2) (A) may expedite the review of applications and inspections with respect to the drug in accordance with section 506C(g); and (B) shall authorize importation of the drug in accordance with section 506C(h). (b) Determination of marginally competitive market (1) In general The Secretary shall determine that a marginally competitive market exists with respect to an applicable drug if\u2014 (A) for at least 2 consecutive months prior to the determination, fewer than 5 drugs approved under section 505(c) (referred to in this paragraph as the \u2018applicable listed drug\u2019) or under section 505(j) that reference the applicable listed drug were commercially available in the United States; (B) the applicable listed drug was approved at least 10 years before such determination; and (C) each patent which claims an active ingredient of the applicable listed drug has expired. (2) Commercially available (A) In general For purposes of paragraph (1)(A), a drug is not commercially available in the United States if\u2014 (i) the holder of an application approved under subsection (c) or (j) of section 505 has publicly announced that it has discontinued the manufacturing of the drug; (ii) a drug approved under subsection (c) or (j) of section 505 has been withdrawn or discontinued; or (iii) the Secretary has any other reasonable basis to conclude that a drug approved under subsection (c) or (j) of section 505 is not competitively relevant. (B) Holder of approved application In determining whether 5 drugs are commercially available under paragraph (1)(A), in the case of a single person who is the holder of more than one application approved as described in paragraph (1)(A) with respect to an applicable drug, only one such drug shall be considered to be commercially available. (c) Applicable drug In this section, the term applicable drug means a drug that is not a radio pharmaceutical drug product or any other product as designated by the Secretary. .\n##### (c) Annual reporting on drug shortages\nSection 506C\u20131(a)(5)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c\u20131(a)(5)(B) ) is amended\u2014\n**(1)**\nin clause (i), by striking ; and and inserting ; ;\n**(2)**\nin clause (ii), by adding and after the semicolon; and\n**(3)**\nby inserting after clause (ii) the following:\n(iii) the number of drugs authorized for temporary importation under section 506C(h); .",
      "versionDate": "2025-07-17",
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
        "updateDate": "2025-09-05T16:35:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
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
          "measure-id": "id119s2345",
          "measure-number": "2345",
          "measure-type": "s",
          "orig-publish-date": "2025-07-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2345v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Short on Competition Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to provide temporary authorization to import certain prescription drugs facing shortages or in a marginally competitive drug market.</p><p>Specifically, the FDA must authorize importation of an eligible drug that is lifesaving, life-sustaining, or intended to treat or prevent a debilitating condition. To be eligible, a drug must (1) be facing a shortage, (2) require a prescription, (3) have received market authorization in certain foreign countries, and (4) have the same active ingredient as the drug for which there is a shortage in the United States. The drug's manufacturer must also seek approval for the drug as a generic drug.</p><p>The authority to import a drug terminates after three years or when\u00a0the shortage no longer applies, whichever occurs first. Importation must begin within 60 days of the FDA receiving an application that meets all of the applicable requirements. The FDA may deny importation of a drug for reasons related to safety or effectiveness.</p><p>Drugs in marginally competitive markets must be treated as being in shortage for the purposes of this bill and may be treated as such for the purposes of expediting inspections and reviewing applications. A drug is in a marginally competitive market if (1) there are fewer than five holders of approved applications for commercially available brand-name or generic versions of the drug, (2) the drug has been approved for at least 10 years, and (3) the patents on the drug's active ingredients have expired.</p>"
        },
        "title": "Short on Competition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2345.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Short on Competition Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to provide temporary authorization to import certain prescription drugs facing shortages or in a marginally competitive drug market.</p><p>Specifically, the FDA must authorize importation of an eligible drug that is lifesaving, life-sustaining, or intended to treat or prevent a debilitating condition. To be eligible, a drug must (1) be facing a shortage, (2) require a prescription, (3) have received market authorization in certain foreign countries, and (4) have the same active ingredient as the drug for which there is a shortage in the United States. The drug's manufacturer must also seek approval for the drug as a generic drug.</p><p>The authority to import a drug terminates after three years or when\u00a0the shortage no longer applies, whichever occurs first. Importation must begin within 60 days of the FDA receiving an application that meets all of the applicable requirements. The FDA may deny importation of a drug for reasons related to safety or effectiveness.</p><p>Drugs in marginally competitive markets must be treated as being in shortage for the purposes of this bill and may be treated as such for the purposes of expediting inspections and reviewing applications. A drug is in a marginally competitive market if (1) there are fewer than five holders of approved applications for commercially available brand-name or generic versions of the drug, (2) the drug has been approved for at least 10 years, and (3) the patents on the drug's active ingredients have expired.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s2345"
    },
    "title": "Short on Competition Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Short on Competition Act</strong></p><p>This bill requires the Food and Drug Administration (FDA) to provide temporary authorization to import certain prescription drugs facing shortages or in a marginally competitive drug market.</p><p>Specifically, the FDA must authorize importation of an eligible drug that is lifesaving, life-sustaining, or intended to treat or prevent a debilitating condition. To be eligible, a drug must (1) be facing a shortage, (2) require a prescription, (3) have received market authorization in certain foreign countries, and (4) have the same active ingredient as the drug for which there is a shortage in the United States. The drug's manufacturer must also seek approval for the drug as a generic drug.</p><p>The authority to import a drug terminates after three years or when\u00a0the shortage no longer applies, whichever occurs first. Importation must begin within 60 days of the FDA receiving an application that meets all of the applicable requirements. The FDA may deny importation of a drug for reasons related to safety or effectiveness.</p><p>Drugs in marginally competitive markets must be treated as being in shortage for the purposes of this bill and may be treated as such for the purposes of expediting inspections and reviewing applications. A drug is in a marginally competitive market if (1) there are fewer than five holders of approved applications for commercially available brand-name or generic versions of the drug, (2) the drug has been approved for at least 10 years, and (3) the patents on the drug's active ingredients have expired.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s2345"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2345is.xml"
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
      "title": "Short on Competition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Short on Competition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow for expedited approval of generic prescription drugs and temporary importation of prescription drugs in the case of marginally competitive drug markets and drug shortages.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:20Z"
    }
  ]
}
```
