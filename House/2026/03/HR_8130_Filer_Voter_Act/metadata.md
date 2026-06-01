# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8130
- Title: Filer Voter Act
- Congress: 119
- Bill type: HR
- Bill number: 8130
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-27T14:31:20Z
- Update date including text: 2026-04-27T14:31:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-26 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-26 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8130",
    "number": "8130",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Filer Voter Act",
    "type": "HR",
    "updateDate": "2026-04-27T14:31:20Z",
    "updateDateIncludingText": "2026-04-27T14:31:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-26T14:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8130ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8130\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mrs. Watson Coleman (for herself, Mr. Tonko , and Mrs. Cherfilus-McCormick ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the National Voter Registration Act of 1993 to treat certain tax return preparers as voter registration agencies under such Act for purposes of distributing voter registration application forms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Filer Voter Registration Act or the Filer Voter Act .\n#### 2. Treatment of tax return preparers as voter registration agencies for purposes of distributing voter registration application forms\n##### (a) Tax return preparers as voter registration agencies\n**(1) In general**\nSection 7 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20506 ) is amended by adding at the end the following new subsection:\n(e) Special rules for tax return preparers (1) Treatment as voter registration agencies Subject to paragraph (2) and except as provided in paragraph (3), each tax return preparer in a State shall be treated as a voter registration agency designated by the State for purposes of this section. (2) Methods of meeting requirements (A) Availability of forms in office for customers who meet preparer in person A tax return preparer who provides tax return preparation services to customers who meet the preparer in person at the preparer\u2019s office may meet the requirements applicable to the tax return preparer under this section by displaying copies of the mail voter registration application form used by the State in which the office is located in a manner which ensures that the forms are visible and accessible to any customer who visits the office. (B) Availability of forms through hyperlink for customers who receive services online A tax return preparer who provides tax return preparation services to customers through online methods may meet the requirements applicable to the tax return preparer under this section\u2014 (i) by providing a hyperlink to the mail voter registration application form developed by the Election Assistance Commission under section 9(a)(2), or to the website of the appropriate election official through which an individual may register to vote online, through the same computer software, service, or program by which the tax return preparer provides services to the customer online; and (ii) by ensuring that the hyperlink is prominently displayed to each customer who receives any tax return preparation services from the tax return preparer. (3) Exceptions A tax return preparer shall not be required to meet the following requirements of this section which are otherwise applicable to a voter registration agency designated by the State for purposes of this section: (A) Clause (iii) of subsection (a)(4)(A) (relating to the acceptance of completed voter registration application forms for transmittal to the appropriate State election official). (B) Subparagraph (B) of subsection (a)(6) (relating to the provision of the form by which an individual may apply to register to vote at a voter registration agency and related forms and statements). (C) Subsection (d) (relating to the deadline for the transmittal of completed voter registration application forms to the appropriate State election official). (4) Definition In this subsection, the term tax return preparer means\u2014 (A) a tax return preparer described in section 7701(a)(36) of the Internal Revenue Code of 1986, other than a tax return preparer who\u2014 (i) during the taxable year, reasonably expects to prepare fewer than 100 individual tax returns; or (ii) during the previous taxable year, prepared fewer than 100 individual tax returns; or (B) any certified volunteer tax preparer who receives funding from the Secretary of the Treasury under the Community Volunteer Income Tax Assistance Matching Grants Program or the Tax Counseling for the Elderly Program. (5) Regulations The Election Assistance Commission, in consultation with the Secretary of the Treasury, shall promulgate such regulations as the Commission considers appropriate to carry out this subsection. .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply with respect to taxable years occurring after December 2021.\n##### (b) Responsibilities of Secretary of the Treasury relating to certified volunteer tax preparers\n**(1) Guidance to certified volunteer tax preparers receiving funding under certain programs**\nThe Secretary of the Treasury shall provide assistance and guidance to enable certified volunteer tax preparers who receive funding under the Community Volunteer Income Tax Assistance Matching Grants Program or the Tax Counseling for the Elderly Program to meet the requirements of section 7(e) of the National Voter Registration Act of 1993 (as added by subsection (a)).\n**(2) Revision to intake and interview and quality review sheet**\nThe Secretary of the Treasury shall revise the intake and interview and quality review sheet provided to an individual who utilizes the services of certified volunteer preparers to include the following question: Do you want to receive a form today to register to vote or update your voter registration information? , as well as a box for the individual to check to indicate whether or not the individual wants to receive such a form.\n**(3) Display of information at sites**\nThe Secretary of the Treasury shall revise the quality site requirements for volunteer tax preparers who receive funding under the Community Volunteer Income Tax Assistance Matching Grants Program or the Tax Counseling for the Elderly Program to include a requirement that the sites clearly and prominently display voter registration application forms.",
      "versionDate": "2026-03-26",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-20T22:21:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-26",
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
          "measure-id": "id119hr8130",
          "measure-number": "8130",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-26",
          "originChamber": "HOUSE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8130v00",
            "update-date": "2026-04-27"
          },
          "action-date": "2026-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Tax Filer Voter Registration Act or the Filer Voter Act</strong></p> <p>This bill treats certain tax return preparers as voter registration agencies. </p> <p>Specifically, the bill requires tax return preparers who prepare at least 100 individual tax returns in a taxable year to provide voter registration application forms to their customers. The form must be made available by (1) displaying copies of the form in the preparer's office for customers who receive in-person services, and (2) providing a hyperlink to the form for customers who receive online services.</p> <p>The bill also outlines the responsibilities of the Department of the Treasury to enable certified volunteer tax preparers to meet the requirements of the bill.</p>"
        },
        "title": "Filer Voter Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8130.xml",
    "summary": {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tax Filer Voter Registration Act or the Filer Voter Act</strong></p> <p>This bill treats certain tax return preparers as voter registration agencies. </p> <p>Specifically, the bill requires tax return preparers who prepare at least 100 individual tax returns in a taxable year to provide voter registration application forms to their customers. The form must be made available by (1) displaying copies of the form in the preparer's office for customers who receive in-person services, and (2) providing a hyperlink to the form for customers who receive online services.</p> <p>The bill also outlines the responsibilities of the Department of the Treasury to enable certified volunteer tax preparers to meet the requirements of the bill.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr8130"
    },
    "title": "Filer Voter Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tax Filer Voter Registration Act or the Filer Voter Act</strong></p> <p>This bill treats certain tax return preparers as voter registration agencies. </p> <p>Specifically, the bill requires tax return preparers who prepare at least 100 individual tax returns in a taxable year to provide voter registration application forms to their customers. The form must be made available by (1) displaying copies of the form in the preparer's office for customers who receive in-person services, and (2) providing a hyperlink to the form for customers who receive online services.</p> <p>The bill also outlines the responsibilities of the Department of the Treasury to enable certified volunteer tax preparers to meet the requirements of the bill.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr8130"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8130ih.xml"
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
      "title": "Filer Voter Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Filer Voter Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Filer Voter Registration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Voter Registration Act of 1993 to treat certain tax return preparers as voter registration agencies under such Act for purposes of distributing voter registration application forms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:52Z"
    }
  ]
}
```
