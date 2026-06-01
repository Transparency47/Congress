# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3842?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3842
- Title: 21st Century WIC Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3842
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-03-04T14:17:47Z
- Update date including text: 2026-03-04T14:17:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3842",
    "number": "3842",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "21st Century WIC Act of 2026",
    "type": "S",
    "updateDate": "2026-03-04T14:17:47Z",
    "updateDateIncludingText": "2026-03-04T14:17:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T20:25:39Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3842is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3842\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Marshall (for himself and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Child Nutrition Act of 1966 to permit video or telephone certifications under the special supplemental nutrition program for women, infants, and children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 21st Century WIC Act of 2026 .\n#### 2. Redefining presence at certification\n##### (a) In general\nSection 17(d)(3) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(d)(3) ) is amended by striking subparagraph (C) and inserting the following:\n(C) Presence for certain determinations and evaluations (i) In general Each individual seeking certification, recertification, or a nutritional risk evaluation for participation in the program authorized under this section shall be provided an appointment that is, at the option of the individual, through any of the following formats: (I) In person. (II) By telephone. (III) Through video technology that permits 2-way, real-time interactive communications. (IV) Through other formats that permit 2-way, real-time interactive communications, as determined by the Secretary. (ii) ADA compliance Any format made available for an appointment under clause (i) shall be accessible to an individual in accordance with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) and section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ). (iii) Nutritional risk evaluations for remote certification If an individual certifies for participation in the program under clause (i) through a format other than in-person, the State agency shall\u2014 (I) plan to collect the anthropometric data necessary to evaluate the nutritional risk of that individual within 30 days of the appointment; and (II) collect such data not later than 90 days after the appointment. (iv) Interim eligibility for nutritional risk (I) In general A State agency may\u2014 (aa) consider an applicant who meets the income eligibility standards under this section to be temporarily eligible on an interim basis to participate in the program authorized under this section; and (bb) temporarily certify that individual for participation in the program immediately, without delaying temporary certification until a nutritional risk evaluation is carried out. (II) Timing for nutritional risk evaluation A nutritional risk evaluation for an individual temporarily certified pursuant to subclause (I) shall be completed not later than 90 days after the date of temporary certification of the individual. (III) Termination of temporary certification The temporary certification of an individual certified pursuant to subclause (I) shall terminate on the earliest of\u2014 (aa) 91 days after the date of temporary certification if the State agency does not collect data on the individual pursuant to clause (iii); and (bb) the date of a determination by the State agency that the individual does not meet the nutritional risk criteria. .\n##### (b) Technical amendment\nSection 17(d)(3) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(d)(3) ) is amended by conforming the margin of subparagraph (B) to the margin of subparagraph (C).\n#### 3. Remote benefit issuance\n##### (a) In general\nSection 17(f)(6)(B) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(f)(6)(B) ) is amended\u2014\n**(1)**\nin the third sentence\u2014\n**(A)**\nby striking vouchers by mail and inserting food instruments by mail, remote issuance, or other means ; and\n**(B)**\nby striking The Secretary and inserting the following:\n(iii) Disapproval of State plan The Secretary ;\n**(2)**\nin the second sentence\u2014\n**(A)**\nby striking vouchers by mail in its plan and inserting food instruments by mail, remote issuance, or other means in the State plan ; and\n**(B)**\nby striking The State and inserting the following:\n(ii) State plan The State ; and\n**(3)**\nby striking (B) State agencies and all that follows through to obtain vouchers. and inserting the following:\n(B) Delivery of food instruments (i) In general State agencies may provide for the delivery of food instruments, including electronic benefit transfer cards, to any participant through means that do not require the participant to travel to the local agency to obtain the food instruments, such as through mailing or remote issuance. .\n##### (b) Regulations\nThe Secretary of Agriculture shall revise section 246.12(r) of title 7, Code of Federal Regulations, by striking paragraph (4).\n#### 4. Report to Congress\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Education and Labor of the House of Representatives a report on the use of remote technologies under the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) (referred to in this section as the program ).\n##### (b) Content of report\nThe report submitted under subsection (a) shall include a description of\u2014\n**(1)**\nthe use of remote technologies and other digital tools, including video, telephone, and online platforms\u2014\n**(A)**\nto certify eligible individuals for program services; and\n**(B)**\nto provide nutrition education and breastfeeding support to program participants;\n**(2)**\nthe impact of remote technologies, including video, telephone, and online platforms, on certifications, appointments, and participant satisfaction under the program; and\n**(3)**\nbest practices\u2014\n**(A)**\nto certify program participants for program services using remote technologies;\n**(B)**\nto incorporate the use of digital tools into the program certification process;\n**(C)**\nto integrate nutrition education and breastfeeding support services for program participants into remote technologies and platforms; and\n**(D)**\nto securely manage program participant data.",
      "versionDate": "2026-02-11",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-03T20:14:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-11",
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
          "measure-id": "id119s3842",
          "measure-number": "3842",
          "measure-type": "s",
          "orig-publish-date": "2026-02-11",
          "originChamber": "SENATE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3842v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2026-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>21st Century WIC Act of 2026</strong></p><p>This bill permanently allows individuals to remotely certify their eligibility for, and receive benefits through, the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>Specifically, the bill requires that a state agency allow\u00a0an individual seeking a WIC certification, recertification, or a nutritional risk evaluation to do so by phone or through video teleconference, in addition to the in-person option.</p><p>A state agency has 90 days to collect data for a nutritional risk evaluation\u00a0for a remotely certified individual. Further, a\u00a0state agency may consider an applicant who meets the income eligibility standards to be\u00a0temporarily eligible on an interim basis\u00a0to participate in the program and may certify the individual for immediate participation without waiting for a nutritional risk evaluation.</p><p>The bill also allows states to provide benefits on WIC electronic benefit transfer cards through mail or remote issuance instead of requiring participants to pick up or reload benefits in person at a WIC office.</p><p>Further, the Department of Agriculture must report to Congress about the use of remote technologies and other digital tools in the WIC program.</p><p>Currently, individuals are generally required to be physically present to certify their WIC eligibility and receive benefits, with exceptions. The Food and Nutrition Service has temporarily waived these requirements and allowed remote certification and benefits using authorities that were originally provided by laws that were enacted to address\u00a0COVID-19.</p>"
        },
        "title": "21st Century WIC Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3842.xml",
    "summary": {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>21st Century WIC Act of 2026</strong></p><p>This bill permanently allows individuals to remotely certify their eligibility for, and receive benefits through, the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>Specifically, the bill requires that a state agency allow\u00a0an individual seeking a WIC certification, recertification, or a nutritional risk evaluation to do so by phone or through video teleconference, in addition to the in-person option.</p><p>A state agency has 90 days to collect data for a nutritional risk evaluation\u00a0for a remotely certified individual. Further, a\u00a0state agency may consider an applicant who meets the income eligibility standards to be\u00a0temporarily eligible on an interim basis\u00a0to participate in the program and may certify the individual for immediate participation without waiting for a nutritional risk evaluation.</p><p>The bill also allows states to provide benefits on WIC electronic benefit transfer cards through mail or remote issuance instead of requiring participants to pick up or reload benefits in person at a WIC office.</p><p>Further, the Department of Agriculture must report to Congress about the use of remote technologies and other digital tools in the WIC program.</p><p>Currently, individuals are generally required to be physically present to certify their WIC eligibility and receive benefits, with exceptions. The Food and Nutrition Service has temporarily waived these requirements and allowed remote certification and benefits using authorities that were originally provided by laws that were enacted to address\u00a0COVID-19.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119s3842"
    },
    "title": "21st Century WIC Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>21st Century WIC Act of 2026</strong></p><p>This bill permanently allows individuals to remotely certify their eligibility for, and receive benefits through, the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC).</p><p>Specifically, the bill requires that a state agency allow\u00a0an individual seeking a WIC certification, recertification, or a nutritional risk evaluation to do so by phone or through video teleconference, in addition to the in-person option.</p><p>A state agency has 90 days to collect data for a nutritional risk evaluation\u00a0for a remotely certified individual. Further, a\u00a0state agency may consider an applicant who meets the income eligibility standards to be\u00a0temporarily eligible on an interim basis\u00a0to participate in the program and may certify the individual for immediate participation without waiting for a nutritional risk evaluation.</p><p>The bill also allows states to provide benefits on WIC electronic benefit transfer cards through mail or remote issuance instead of requiring participants to pick up or reload benefits in person at a WIC office.</p><p>Further, the Department of Agriculture must report to Congress about the use of remote technologies and other digital tools in the WIC program.</p><p>Currently, individuals are generally required to be physically present to certify their WIC eligibility and receive benefits, with exceptions. The Food and Nutrition Service has temporarily waived these requirements and allowed remote certification and benefits using authorities that were originally provided by laws that were enacted to address\u00a0COVID-19.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119s3842"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3842is.xml"
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
      "title": "21st Century WIC Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T03:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "21st Century WIC Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Child Nutrition Act of 1966 to permit video or telephone certifications under the special supplemental nutrition program for women, infants, and children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:25Z"
    }
  ]
}
```
