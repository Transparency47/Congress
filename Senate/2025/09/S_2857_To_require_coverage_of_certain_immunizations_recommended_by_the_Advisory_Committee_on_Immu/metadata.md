# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2857?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2857
- Title: Protecting Free Vaccines Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2857
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-05-12T20:07:24Z
- Update date including text: 2026-05-12T20:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2857",
    "number": "2857",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Protecting Free Vaccines Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T20:07:24Z",
    "updateDateIncludingText": "2026-05-12T20:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
            "date": "2025-09-18T15:04:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T15:04:14Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-18",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2857is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2857\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Wyden (for himself and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices under the Medicare program, the Medicaid program, the Children\u2019s Health Insurance Program, group health plans, and health insurance coverage.\n#### 1. Short title\nThis Act may be cited as the Protecting Free Vaccines Act of 2025 .\n#### 2. Requiring coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices\n##### (a) Group health plans and health insurance coverage\n**(1) PHSA**\n**(A) In general**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices (a) In general With respect to plan years occurring during the date of the enactment of this section, or beginning on or after the date of the enactment of this section and before January 1, 2030, a group health plan and a health insurance issuer offering group or individual health insurance coverage shall provide coverage for and shall not impose any cost sharing requirements for immunizations that had in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved as of October 25, 2024, including such an immunization involving a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 on or before such date. (b) Special rule Subsection (a) shall not apply in the case of an immunization administered during the minimum interval established under section 2713(b) with respect to such immunization. .\n**(B) Conforming amendment**\nSection 1302(e)(1)(B)(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(e)(1)(B)(i) ) is amended by striking section 2713 and inserting sections 2713 and 2799A\u201311 of the Public Health Service Act .\n**(2) ERISA**\n**(A) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following new section:\n726. Coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices (a) In general With respect to plan years occurring during the date of the enactment of this section, or beginning on or after the date of the enactment of this section and before January 1, 2030, a group health plan and a health insurance issuer offering group health insurance coverage shall provide coverage for and shall not impose any cost sharing requirements for immunizations that had in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved as of October 25, 2024, including such an immunization involving a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) on or before such date. (b) Special rule Subsection (a) shall not apply in the case of an immunization administered during the minimum interval established under section 2713(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201313(b) ) with respect to such immunization. .\n**(B) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 note) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices. .\n**(3) IRC**\n**(A) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9826. Coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices (a) In general With respect to plan years occurring during the date of the enactment of this section, or beginning on or after the date of the enactment of this section and before January 1, 2030, a group health plan shall provide coverage for and shall not impose any cost sharing requirements for immunizations that had in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved as of October 25, 2024, including such an immunization involving a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) on or before such date. (b) Special rule Subsection (a) shall not apply in the case of an immunization administered during the minimum interval established under section 2713(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201313(b) ) with respect to such immunization. .\n**(B) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9826. Coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices. .\n##### (b) Medicare\nSection 1860D\u20132(b)(8)(B) of the Social Security Act ( 42 U.S.C. 1395w\u2013102(b)(8)(B) ) is amended\u2014\n**(1)**\nby striking with recommendations and inserting\nwith\u2014 (i) recommendations ;\n**(2)**\nby striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new clause:\n(ii) for plan years occurring during the date of the enactment of this clause, or beginning on or after the date of the enactment of this clause and before January 1, 2030, in the case of a vaccine with respect to which such a recommendation is revoked with respect to the individual involved on or after October 25, 2024, including such a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act on or before such date, the most recent recommendation that was in effect with respect to such vaccine and such individual prior to such revocation. .\n##### (c) Medicaid\n**(1) In general**\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(A)**\nin subsection (a)(13)(B)\u2014\n**(i)**\nby striking individual, approved and inserting\nindividual\u2014 (i) approved ; and\n**(ii)**\nby adding at the end the following new clause:\n(ii) for the period beginning on the date of the enactment of this clause and ending on December 31, 2029, approved vaccines, and the administration of such vaccines, that were recommended by such advisory committee with respect to the individual involved as of October 25, 2024, including such a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act on or before such date; and ; and\n**(B)**\nin subsection (r)(1)(B)(iii), by\u2014\n**(i)**\nstriking section 1928(c)(2)(B)(i) and inserting clause (i) of section 1928(c)(2)(B) ; and\n**(ii)**\ninserting , subject to the limitation described in clause (iii) of such section after pediatric vaccines .\n**(2) Coverage for pregnant individuals**\nSection 1902(a)(10) of the Social Security Act ( 42 U.S.C. 1396a(a)(10) ) is amended in the matter following subparagraph (G) by inserting medical assistance for vaccines described in section 1905(a)(13)(B) and the administration of such vaccines, after complicate pregnancy, .\n**(3) Program for distribution of pediatric vaccines**\nSection 1928 of the Social Security Act ( 42 U.S.C. 1396s ) is amended\u2014\n**(A)**\nin subsection (c)(2)(B)\u2014\n**(i)**\nin clause (i), by striking clause (ii) and inserting clauses (ii) and (iii) ; and\n**(ii)**\nby adding at the end the following new clause:\n(iii) For the period beginning on the date of the enactment of this clause and ending on December 31, 2029, the provider will not take into account any change in the schedule described in clause (i) that removes the recommendation to administer a pediatric vaccine with respect to the vaccine-eligible child involved if such pediatric vaccine was recommended with respect to such child under such schedule as of October 25, 2024, including with respect to such pediatric vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act on or before such date. ; and\n**(B)**\nin subsection (e), by inserting For purposes of the preceding sentence, during the period beginning on the date of the enactment of this sentence and ending on December 31, 2029, the Secretary may not take into account any revision of such list that occurs on or after October 25, 2024, that removes a pediatric vaccine from such list if such vaccine was included in such list as of such date, including with respect to such vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act on or before such date. after the period at the end.\n**(4) State flexibility in benefit packages**\nSection 1937(b) of the Social Security Act ( 42 U.S.C. 1396u\u20137(b) ) is amended by adding at the end the following new paragraph:\n(9) Coverage of adult vaccines Notwithstanding the previous provisions of this section, a State may not provide for medical assistance through enrollment of an individual with benchmark coverage or benchmark-equivalent coverage under this section unless such coverage includes (and does not impose any deduction, cost sharing, or similar charge for) the medical assistance described in section 1905(a)(13)(B). .\n##### (d) CHIP\nSection 2103 of the Social Security Act ( 42 U.S.C. 1397cc ) is amended\u2014\n**(1)**\nin subsection (c), by adding at the end the following new paragraph:\n(13) Required coverage of certain vaccines recommended by the Advisory Committee on Immunization Practices Regardless of the type of coverage elected by a State under subsection (a), the child health assistance provided for a targeted low-income child shall include coverage, during the period beginning on the date of the enactment of this paragraph and ending on December 31, 2029, of vaccines, and the administration of such vaccines, that had in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the child involved as of October 25, 2024, including such a vaccine as updated or changed after such date under an approved supplemental application to a biological product licensed under section 351 of the Public Health Service Act on or before such date. ; and\n**(2)**\nin subsection (e)(2), by inserting vaccines described in subsection (c)(13) administered during the period beginning on the date of the enactment of such subsection and ending on December 31, 2029 (and the administration of such vaccines), before services described in section 1916(a)(2)(G) .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5448",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Free Vaccines Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
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
        "updateDate": "2026-04-17T15:45:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119s2857",
          "measure-number": "2857",
          "measure-type": "s",
          "orig-publish-date": "2025-09-18",
          "originChamber": "SENATE",
          "update-date": "2026-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2857v00",
            "update-date": "2026-05-12"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Free Vaccines Act\u00a0of 2025\u00a0</strong></p><p>This bill requires Medicare, Medicaid, the Children's Health Insurance Program (CHIP), and private health insurers to cover, without cost-sharing, vaccines that were recommended by the Centers for Disease Control and Prevention's Advisory Committee on Immunization Practices as of October 25, 2024. The requirement ends on January 1, 2030.</p>"
        },
        "title": "Protecting Free Vaccines Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2857.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Free Vaccines Act\u00a0of 2025\u00a0</strong></p><p>This bill requires Medicare, Medicaid, the Children's Health Insurance Program (CHIP), and private health insurers to cover, without cost-sharing, vaccines that were recommended by the Centers for Disease Control and Prevention's Advisory Committee on Immunization Practices as of October 25, 2024. The requirement ends on January 1, 2030.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119s2857"
    },
    "title": "Protecting Free Vaccines Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Free Vaccines Act\u00a0of 2025\u00a0</strong></p><p>This bill requires Medicare, Medicaid, the Children's Health Insurance Program (CHIP), and private health insurers to cover, without cost-sharing, vaccines that were recommended by the Centers for Disease Control and Prevention's Advisory Committee on Immunization Practices as of October 25, 2024. The requirement ends on January 1, 2030.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119s2857"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2857is.xml"
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
      "title": "Protecting Free Vaccines Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Free Vaccines Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require coverage of certain immunizations recommended by the Advisory Committee on Immunization Practices under the Medicare program, the Medicaid program, the Children's Health Insurance Program, group health plans, and health insurance coverage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:30Z"
    }
  ]
}
```
