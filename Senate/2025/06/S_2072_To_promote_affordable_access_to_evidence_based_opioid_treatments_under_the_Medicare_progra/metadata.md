# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2072?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2072
- Title: MORE Savings Act
- Congress: 119
- Bill type: S
- Bill number: 2072
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-25T16:25:33Z
- Update date including text: 2025-07-25T16:25:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2072",
    "number": "2072",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "MORE Savings Act",
    "type": "S",
    "updateDate": "2025-07-25T16:25:33Z",
    "updateDateIncludingText": "2025-07-25T16:25:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T19:31:53Z",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2072is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2072\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Blumenthal (for himself, Mr. Fetterman , Mr. Heinrich , Mr. Luj\u00e1n , Ms. Klobuchar , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo promote affordable access to evidence-based opioid treatments under the Medicare program and require coverage of medication assisted treatment for opioid use disorders, opioid overdose reversal medications, and recovery support services by health plans without cost-sharing requirements.\n#### 1. Short title\nThis Act may be cited as the Maximizing Opioid Recovery Emergency Savings Act or the MORE Savings Act .\n#### 2. Testing of elimination of Medicare cost-sharing for evidence-based opioid treatments\nSection 1115A(b)(2) of the Social Security Act ( 42 U.S.C. 1315a(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), in the last sentence, by inserting , and shall include the model described in subparagraph (D) (which shall be implemented by not later than six months after the date of the enactment of the Maximizing Opioid Recovery Emergency Savings Act) before the period at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(D) Affordable access to evidence-based opioid treatments (i) In general The model described in this subparagraph is a model that seeks to provide affordable access to evidence-based opioid treatments and community-based recovery support services by eliminating coinsurance, copayments, and deductibles otherwise applicable under parts B and D of title XVIII (including as such parts are applied under part C of such title) for the following items and services that are otherwise covered under such parts: (I) Drugs and biologicals prescribed or furnished to treat opioid use disorders or reverse overdose. (II) Behavioral health and community support services furnished for the treatment of opioid use disorders, including treatment of addiction in non-hospital residential facilities licensed to furnish such treatment. (III) Recovery support services to maintain a healthy lifestyle following opioid misuse treatment, such as peer counseling and transportation. (ii) Selection of sites The CMI shall select 15 States in which to conduct the model under this subparagraph. A State shall meet each of the following criteria in order to be selected under the preceding sentence: (I) The State has a high proportion of Medicare beneficiaries. (II) The State has a high rate of overdose deaths due to opioids. (III) The State has a significant percentage of rural areas. (iii) Termination and modification provision not applicable for first five years of the model The provisions of paragraph (3)(B) shall apply to the model under this subparagraph beginning on the date that is five years after such model is implemented, but shall not apply to such model prior to such date. .\n#### 3. Coverage of opioid treatments\n##### (a) In general\n**(1) PHSA**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following:\n2799A\u201311. Coverage of opioid treatments A group health plan and a health insurance issuer offering group or individual health insurance coverage shall, at a minimum, with respect to a participant, beneficiary, or enrollee in the plan or coverage, provide coverage for and shall not impose any cost-sharing requirements for\u2014 (1) prescription drugs for the treatment of opioid use disorders or to reverse overdose; (2) behavioral health services for the treatment of opioid use disorders, including treatment of opioid use disorders in non-hospital residential facilities licensed to provide such treatment; or (3) community recovery support services that are provided in conjunction with, where appropriate, medication-assisted treatment for an opioid use disorder, such as peer counseling and transportation, to support the participant, beneficiary, or enrollee in maintaining a healthy lifestyle following opioid misuse treatment. .\n**(2) ERISA**\n**(A) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following:\n726. Coverage of opioid treatments A group health plan and a health insurance issuer offering group health insurance coverage shall, at a minimum, with respect to a participant or beneficiary in the plan or coverage, provide coverage for and shall not impose any cost-sharing requirements for\u2014 (1) prescription drugs for the treatment of opioid use disorders or to reverse overdose; (2) behavioral health services for the treatment of opioid use disorders, including treatment of opioid use disorders in non-hospital residential facilities licensed to provide such treatment; or (3) community recovery support services that are provided in conjunction with, where appropriate, medication-assisted treatment for an opioid use disorder, such as peer counseling and transportation, to support the participant or beneficiary in maintaining a healthy lifestyle following opioid misuse treatment. .\n**(B) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Coverage of opioid treatments. .\n**(3) IRC**\n**(A) In general**\nChapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n9826. Coverage of opioid treatments A group health plan shall, at a minimum, with respect to a participant or beneficiary in the plan, provide coverage for and shall not impose any cost-sharing requirements for\u2014 (1) prescription drugs for the treatment of opioid use disorders or to reverse overdose; (2) behavioral health services for the treatment of opioid use disorders, including treatment of opioid use disorders in non-hospital residential facilities licensed to provide such treatment; or (3) community recovery support services that are provided in conjunction with, where appropriate, medication-assisted treatment for an opioid use disorder, such as peer counseling and transportation, to support the participant or beneficiary in maintaining a healthy lifestyle following opioid misuse treatment. .\n**(B) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9826. Coverage of opioid treatments.\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2027.\n#### 4. Enhanced Federal match for medication-assisted treatment and recovery support services under Medicaid\n##### (a) In general\nSection 1905(b) of the Social Security Act ( 42 U.S.C. 1396d(b) ) is amended by adding at the end the following: Notwithstanding the first sentence of this subsection, during the portion of the period described in subsection (a)(29) that begins on the date of enactment of this sentence, the Federal medical assistance percentage shall be 90 percent with respect to amounts expended during such portion of such period by a State that is one of the 50 States or the District of Columbia as medical assistance for medication-assisted treatment (as defined in subsection (ee)(1)). .\n##### (b) State option To provide recovery support services as part of medication-Assisted treatment\nSection 1905(ee)(1) of the Social Security Act ( 42 U.S.C. 1396d(ee)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) at the option of a State, includes recovery support services, such as peer counseling and transportation, that are provided to an individual in conjunction with the provision of such drugs and biological products to support the individual in maintaining a healthy lifestyle following opioid misuse treatment. .",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-07-14T14:31:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119s2072",
          "measure-number": "2072",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2072v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Maximizing Opioid Recovery Emergency Savings Act or the MORE Savings Act</strong></p><p>This bill modifies coverage of opioid treatments and recovery support services under Medicare, Medicaid, and private health insurance.</p><p>Specifically, the bill requires the Center for Medicare and Medicaid Innovation to test a model in which specified opioid treatments and recovery support services are provided under Medicare without cost-sharing (e.g., coinsurance, copayments, and deductibles).</p><p>The bill also allows state Medicaid programs to cover recovery support services as part of medication-assisted treatment (MAT) and increases the applicable Federal Medical Assistance Percentage for MAT.</p><p>Additionally, beginning in 2027, private health insurers must cover specified opioid treatments and MAT-associated recovery support services without cost-sharing.</p>"
        },
        "title": "MORE Savings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2072.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maximizing Opioid Recovery Emergency Savings Act or the MORE Savings Act</strong></p><p>This bill modifies coverage of opioid treatments and recovery support services under Medicare, Medicaid, and private health insurance.</p><p>Specifically, the bill requires the Center for Medicare and Medicaid Innovation to test a model in which specified opioid treatments and recovery support services are provided under Medicare without cost-sharing (e.g., coinsurance, copayments, and deductibles).</p><p>The bill also allows state Medicaid programs to cover recovery support services as part of medication-assisted treatment (MAT) and increases the applicable Federal Medical Assistance Percentage for MAT.</p><p>Additionally, beginning in 2027, private health insurers must cover specified opioid treatments and MAT-associated recovery support services without cost-sharing.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2072"
    },
    "title": "MORE Savings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maximizing Opioid Recovery Emergency Savings Act or the MORE Savings Act</strong></p><p>This bill modifies coverage of opioid treatments and recovery support services under Medicare, Medicaid, and private health insurance.</p><p>Specifically, the bill requires the Center for Medicare and Medicaid Innovation to test a model in which specified opioid treatments and recovery support services are provided under Medicare without cost-sharing (e.g., coinsurance, copayments, and deductibles).</p><p>The bill also allows state Medicaid programs to cover recovery support services as part of medication-assisted treatment (MAT) and increases the applicable Federal Medical Assistance Percentage for MAT.</p><p>Additionally, beginning in 2027, private health insurers must cover specified opioid treatments and MAT-associated recovery support services without cost-sharing.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2072"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2072is.xml"
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
      "title": "MORE Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MORE Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maximizing Opioid Recovery Emergency Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote affordable access to evidence-based opioid treatments under the Medicare program and require coverage of medication assisted treatment for opioid use disorders, opioid overdose reversal medications, and recovery support services by health plans without cost-sharing requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:18:57Z"
    }
  ]
}
```
