# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1023
- Title: RIFA Act
- Congress: 119
- Bill type: HR
- Bill number: 1023
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-10-09T03:26:16Z
- Update date including text: 2025-10-09T03:26:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1023",
    "number": "1023",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "RIFA Act",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:16Z",
    "updateDateIncludingText": "2025-10-09T03:26:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1023ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1023\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Owens (for himself and Mr. Harris of North Carolina ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require disclosure of certain foreign investments within endowments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reporting on Investments in Foreign Adversaries Act or the RIFA Act .\n#### 2. Investment disclosure report\n##### (a) In general\nPart B of title I of the Higher Education Act of 1965 ( 20 U.S.C. 1011 et seq. ) is amended by inserting after section 117 the following:\n117A. Investment disclosure report (a) Investment disclosure report A specified institution shall file a disclosure report in accordance with subsection (b) with the Secretary on each July 31 immediately following any calendar year in which the specified institution purchases, sells, or holds (directly or indirectly through any chain of ownership) one or more investments of concern. (b) Contents of report Each report to the Secretary required by subsection (a) shall contain, with respect to the calendar year preceding the calendar year in which such report is filed, the following information: (1) A list of the investments of concern purchased, sold, or held during such calendar year. (2) The aggregate fair market value of all investments of concern held as of the close of such calendar year. (3) The combined value of all investments of concern sold over the course of such calendar year, as measured by the fair market value of such investments at the time of the sale. (4) The combined value of all capital gains from such sales of investments of concern. (c) Treatment of certain pooled investments (1) Pooled investment classification (A) In general For purposes of this section, except as provided in subparagraph (B), a specified interest acquired by a specified institution in a regulated investment company, exchange traded fund, or any other pooled investment that holds an investment of concern shall be treated as an investment of concern and shall be reported pursuant to paragraph (2)(A). (B) Certification of pooled investment Notwithstanding subparagraph (A), such specified interest shall not be subject to subparagraph (A) if the Secretary certifies, pursuant to paragraph (2)(B), that such pooled investment is not holding an investment of concern. (2) Procedures The Secretary, after consultation with the Secretary of the Treasury and the Securities and Exchange Commission, shall establish procedures under which a pooled investment described in paragraph (1)\u2014 (A) shall be reported in accordance with the requirements of subsection (b); and (B) may be certified under paragraph (1)(B) as not holding an investment of concern. (d) Treatment of related organizations For purposes of this section, assets held by any related organization (as defined in section 4968(d)(2) of the Internal Revenue Code of 1986) with respect to a specified institution shall be treated as held by such specified institution, except that\u2014 (1) such assets shall not be taken into account with respect to more than 1 specified institution; and (2) unless such organization is controlled by such institution or is described in section 509(a)(3) of the Internal Revenue Code of 1986 with respect to such institution, assets which are not intended or available for the use or benefit of such specified institution shall not be taken into account. (e) Valuation of debt For purposes of this section, the fair market value of any debt shall be the principal amount of such debt. (f) Regulations The Secretary, after consultation with the Secretary of the Treasury and the Securities and Exchange Commission, may issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations or other guidance providing for the proper application of this section with respect to certain regulated investment companies, exchange traded funds, and pooled investments. (g) Compliance officer Any specified institution that is required to submit a report under subsection (a) shall designate, before the submission of such report, and maintain a compliance officer, who shall\u2014 (1) be a current employee or legally authorized agent of such institution; and (2) be responsible, on behalf of the institution, for personally certifying accurate compliance with the reporting requirements under this section. (h) Database requirement Beginning not later than the May 31 of the calendar year following the date of enactment of the RIFA Act, the Secretary shall\u2014 (1) establish and maintain a searchable database on a website of the Department, under which all reports submitted under this section\u2014 (A) are made publicly available (in electronic and downloadable format), including any information provided in such reports; (B) can be individually identified and compared; and (C) are searchable and sortable; and (2) not later than 30 days after receipt of a disclosure report under this section, include such report in such database. (i) Enforcement (1) Investigation The Secretary (acting through the General Counsel of the Department) shall conduct investigations of possible violations of this section by institutions and, whenever it appears that an institution has knowingly or willfully failed to comply with a requirement of this section (including any rule or regulation promulgated under such section), shall request that the Attorney General bring a civil action in accordance with paragraph (2). (2) Civil action Whenever it appears that an institution has knowingly or willfully failed to comply with a requirement of this section (including any rule or regulation promulgated under any such section) based on an investigation under paragraph (1), a civil action shall be brought by the Attorney General, at the request of the Secretary, in an appropriate district court of the United States, or the appropriate United States court of any territory or other place subject to the jurisdiction of the United States, to request such court to compel compliance with the requirement of this section. (3) Costs and other fines An institution that is compelled to comply with a requirement of this section pursuant to paragraph (2) shall\u2014 (A) pay to the Treasury of the United States the full costs to the United States of obtaining compliance with the requirement of this section, including all associated costs of investigation and enforcement; and (B) be subject to the applicable fines described in paragraph (4). (4) Fines for violations The Secretary shall impose a fine on an institution that is compelled to comply with a requirement of this section pursuant to paragraph (2) as follows: (A) First-time violations In the case of a specified institution that knowingly or willfully fails to comply with a requirement of this section with respect to a calendar year, and that has not previously knowingly or willfully failed to comply with such a requirement, the Secretary shall impose a fine on the institution in an amount that is not less than 50 percent and not more than 100 percent of the sum of\u2014 (i) the aggregate fair market value of all investments of concern held by such institution as of the close of such calendar year; and (ii) the combined value of all investments of concern sold over the course of such calendar year, as measured by the fair market value of such investments at the time of the sale. (B) Subsequent violations In the case of a specified institution that has been fined pursuant to subparagraph (A) with respect to a calendar year, and that knowingly or willfully fails to comply with a requirement of this section with respect to any additional calendar year, the Secretary shall impose a fine on the institution with respect to any such additional calendar year in an amount that is not less than 100 percent and not more than 200 percent of the sum of\u2014 (i) the aggregate fair market value of all investments of concern held by such institution as of the close of such additional calendar year; and (ii) the combined value of all investments of concern sold over the course of such additional calendar year, as measured by the fair market value of such investments at the time of the sale. (j) Definitions In this section: (1) Foreign country of concern The term foreign country of concern means the following: (A) Any covered nation defined in section 4872 of title 10, United States Code. (B) Any country the Secretary, in consultation with the Secretary of Defense, the Secretary of State, and the Director of National Intelligence, determines, for purposes of this section, to be engaged in conduct that is detrimental to the national security or foreign policy of the United States. (2) Foreign entity of concern The term foreign entity of concern has the meaning given such term in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) ) and includes a foreign entity that is identified on the list published under section 1286(c)(8)(A) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 (10 U.S.C. 22 4001 note; Public Law 115\u2013232 ). (3) Institution The term institution means an institution of higher education (as such term is defined in section 102, other than an institution described in subsection (a)(1)(c) of such section). (4) Investment of concern (A) In general The term investment of concern means any specified interest with respect to any of the following: (i) A foreign country of concern. (ii) A foreign entity of concern. (B) Specified interest The term specified interest means, with respect to any entity\u2014 (i) stock or any other equity or profits interest of such entity; (ii) debt issued by such entity; and (iii) any contract or derivative with respect to any property described in clause (i) or (ii). (5) Specified institution (A) In general The term specified institution , as determined with respect to any calendar year, means an institution if\u2014 (i) such institution is not a public institution; and (ii) the aggregate fair market value of\u2014 (I) the assets held by such institution at the end of such calendar year (other than those assets which are used directly in carrying out the institution\u2019s exempt purpose) is in excess of $6,000,000,000; or (II) the investments of concern held by such institution at the end of such calendar year is in excess of $250,000,000. (B) References to certain terms For the purpose of applying the definition under subparagraph (A), the terms aggregate fair market value and assets which are used directly in carrying out the institution\u2019s exempt purpose shall be applied in the same manner as such terms are applied for the purposes of section 4968(b)(1)(D) of the Internal Revenue Code of 1986. .\n##### (b) Program participation agreement\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094 ) is amended by adding at the end the following:\n(30) (A) An institution will comply with the requirements of section 117A. (B) An institution that, for 3 consecutive institutional fiscal years, violates any requirement of section 117A shall\u2014 (i) be ineligible to participate in the programs authorized by this title for a period of not less than 2 institutional fiscal years; and (ii) in order to regain eligibility to participate in such programs, demonstrate compliance with all requirements of such section for not less than 2 institutional fiscal years after the institutional fiscal year in which such institution became ineligible. .",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-03-31",
        "text": "Received in the Senate and Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1048",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DETERRENT Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-14T17:52:40Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-14T17:52:24Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-04-14T17:52:17Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-14T17:52:33Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-14T17:52:09Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-04-14T17:52:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-07T16:52:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "House",
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
          "measure-id": "id119hr1023",
          "measure-number": "1023",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1023v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reporting on Investments in Foreign Adversaries Act or the RIFA Act</strong></p><p>This bill requires private institutions of higher education (IHEs) with specified assets or investments involving foreign countries or entities of concern\u00a0to file annual investment disclosure reports. The bill applies to a private IHE with (1) assets in excess of $6 billion, or (2) investments of concern in excess of $250 million.\u00a0</p><p>Specifically, the bill requires such a private\u00a0IHE to file a disclosure report with the Department of Education (ED) for a year in which the IHE purchases, sells, or holds one or more investments of concern. <em>Investment of concern</em> means any specified interest (e.g., stock or debt) with respect to a foreign country of concern (e.g., North Korea, China, Russia, or Iran) or a foreign entity of concern (e.g., a foreign entity that is designated as a foreign terrorist organization).\u00a0</p><p>Additionally, the bill requires ED to establish and maintain a publicly available and searchable database with these disclosure reports.</p><p>The bill requires\u00a0ED to investigate possible violations of this bill and outlines the various penalties for each violation.\u00a0Penalties may include losing eligibility for federal student financial aid.</p>"
        },
        "title": "RIFA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1023.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reporting on Investments in Foreign Adversaries Act or the RIFA Act</strong></p><p>This bill requires private institutions of higher education (IHEs) with specified assets or investments involving foreign countries or entities of concern\u00a0to file annual investment disclosure reports. The bill applies to a private IHE with (1) assets in excess of $6 billion, or (2) investments of concern in excess of $250 million.\u00a0</p><p>Specifically, the bill requires such a private\u00a0IHE to file a disclosure report with the Department of Education (ED) for a year in which the IHE purchases, sells, or holds one or more investments of concern. <em>Investment of concern</em> means any specified interest (e.g., stock or debt) with respect to a foreign country of concern (e.g., North Korea, China, Russia, or Iran) or a foreign entity of concern (e.g., a foreign entity that is designated as a foreign terrorist organization).\u00a0</p><p>Additionally, the bill requires ED to establish and maintain a publicly available and searchable database with these disclosure reports.</p><p>The bill requires\u00a0ED to investigate possible violations of this bill and outlines the various penalties for each violation.\u00a0Penalties may include losing eligibility for federal student financial aid.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr1023"
    },
    "title": "RIFA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reporting on Investments in Foreign Adversaries Act or the RIFA Act</strong></p><p>This bill requires private institutions of higher education (IHEs) with specified assets or investments involving foreign countries or entities of concern\u00a0to file annual investment disclosure reports. The bill applies to a private IHE with (1) assets in excess of $6 billion, or (2) investments of concern in excess of $250 million.\u00a0</p><p>Specifically, the bill requires such a private\u00a0IHE to file a disclosure report with the Department of Education (ED) for a year in which the IHE purchases, sells, or holds one or more investments of concern. <em>Investment of concern</em> means any specified interest (e.g., stock or debt) with respect to a foreign country of concern (e.g., North Korea, China, Russia, or Iran) or a foreign entity of concern (e.g., a foreign entity that is designated as a foreign terrorist organization).\u00a0</p><p>Additionally, the bill requires ED to establish and maintain a publicly available and searchable database with these disclosure reports.</p><p>The bill requires\u00a0ED to investigate possible violations of this bill and outlines the various penalties for each violation.\u00a0Penalties may include losing eligibility for federal student financial aid.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr1023"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1023ih.xml"
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
      "title": "RIFA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RIFA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reporting on Investments in Foreign Adversaries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require disclosure of certain foreign investments within endowments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T13:18:27Z"
    }
  ]
}
```
