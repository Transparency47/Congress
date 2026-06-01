# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7727
- Title: Sustaining Rural Healthcare Act
- Congress: 119
- Bill type: HR
- Bill number: 7727
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-03-04T15:50:58Z
- Update date including text: 2026-03-04T15:50:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7727",
    "number": "7727",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Sustaining Rural Healthcare Act",
    "type": "HR",
    "updateDate": "2026-03-04T15:50:58Z",
    "updateDateIncludingText": "2026-03-04T15:50:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T14:32:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "HI"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7727ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7727\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mr. Alford (for himself, Mr. Thompson of Pennsylvania , Ms. Tokuda , and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to ensure the continued designation of certain critical access hospitals under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sustaining Rural Healthcare Act .\n#### 2. Ensuring the continued designation of certain critical access hospitals under the Medicare program\nSection 1820(c)(2) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2) ) is amended by adding at the end the following new subparagraph:\n(F) Ensuring continued designation of certain critical access hospitals A facility that is designated as a critical access hospital by a State under subparagraph (B) that meets the criterion specified in clause (i)(I) as of the date of such designation and that would continue to be eligible for such designation but for application of such criterion shall be deemed to meet such criterion for a period specified by the Secretary (not to exceed 3 years) if the Secretary determines that loss of such designation would reduce access to necessary health care items and services for individuals residing in the service area of such facility. .\n#### 3. Discretionary authority for stabilization parity\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary may designate a hospital as a Critical Access in Character for purposes of Medicare reimbursement if the Secretary determines that the hospital is critical to ensuring access to essential health services in the community it serves.\n##### (b) Eligibility criteria\nA hospital may qualify for designation under subsection (a) if the hospital\u2014\n**(1)**\nis located in a rural area, as defined under section 1886(d)(2)(D) of the Social Security Act or a rural census tract of a metropolitan statistical area (as determined under the most recent modification of the Goldsmith Modification, originally published in the Federal Register on February 27, 1992 (57 Fed. Reg. 6725));\n**(2)**\nis located in an area designated by the Secretary as a health professional shortage area;\n**(3)**\nserves medically underserved, persistent poverty, Tribal, or frontier communities;\n**(4)**\nserves a high proportion of Medicare beneficiaries, as determined by the Secretary based on the percentage of inpatient or outpatient encounters attributable to individuals entitled to benefits under Medicare; and\n**(5)**\nfaces a significant risk of full or partial closure or a material reduction in the scope of services furnished, as determined by the Secretary using financial or operational performance indicators.\n##### (c) Payment parity authority\nA hospital receiving a designation under this section shall, for the period of such designation, be eligible to receive reimbursement for inpatient and outpatient services under Medicare at payment rates equivalent to those applicable to a Critical Access Hospital, subject to such limitations and conditions as the Secretary may establish.\n##### (d) Duration\nA designation under this section shall remain in effect only until the hospital is financially and operationally stabilized, as determined by the Secretary, but may not extend beyond a period of 3 years unless renewed by the Secretary for good cause.\n##### (e) Guidance and implementation\nNot later than 12 months after the date of enactment, the Secretary shall issue guidance describing eligibility standards, documentation requirements, and renewal conditions; establish monitoring and reporting requirements to ensure performance, patient access, and financial stability improvements during the stabilization period; and collaborate with the Department of Agriculture to make available no-cost Technical Assistance through the Community Facilities Program to designated hospitals to strengthen their financial and operational status.\n##### (f) No adverse precedent\nA designation under this section shall not be construed as conferring Critical Access Hospital status for purposes of any other provision of law.\n##### (g) Financial risk standard\nIn conducting a review under subsection (a), the Secretary shall determine whether the hospital is at significant financial risk of reduced access to essential health services in the community it serves. Such determination shall be based on evidence that the hospital\u2019s financial distress\u2014\n**(1)**\nresults primarily from the unique operational challenges of furnishing health care in a rural area, including low patient volumes, workforce shortages, geographic isolation, or payer mix characteristics typical of rural communities; and\n**(2)**\ndoes not result primarily from improper financial management, including but not limited to misallocation of resources, avoidable administrative inefficiencies, or non rural business decisions unrelated to the provision of rural health services.\n##### (h) Documentation\nThe Secretary may require the hospital to submit such financial statements, operational data, and other documentation as the Secretary determines necessary to evaluate the criteria described in subsection (b).\n##### (i) Rule of construction\nNothing in this section shall be construed to limit the Secretary\u2019s authority to impose additional conditions or oversight necessary to ensure the integrity of the Critical Access Hospital program.",
      "versionDate": "2026-02-26",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-03-04T15:50:57Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7727ih.xml"
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
      "title": "Sustaining Rural Healthcare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sustaining Rural Healthcare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to ensure the continued designation of certain critical access hospitals under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:26Z"
    }
  ]
}
```
