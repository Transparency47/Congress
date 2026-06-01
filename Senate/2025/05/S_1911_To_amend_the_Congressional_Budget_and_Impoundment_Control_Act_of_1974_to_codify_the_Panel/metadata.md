# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1911?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1911
- Title: HEALTH Panel Act
- Congress: 119
- Bill type: S
- Bill number: 1911
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T22:49:54Z
- Update date including text: 2025-12-05T22:49:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Budget.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Budget.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1911",
    "number": "1911",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "HEALTH Panel Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:54Z",
    "updateDateIncludingText": "2025-12-05T22:49:54Z"
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
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Budget.",
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
          "date": "2025-05-22T19:56:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1911is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1911\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Ricketts introduced the following bill; which was read twice and referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to codify the Panel of Health Advisors within the Congressional Budget Office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Equipping And Lending Technical Help Panel Act or the HEALTH Panel Act .\n#### 2. Congressional Budget Office Panel of Health Advisors\n##### (a) In general\nTitle II of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n204. Panel of Health Advisors (a) In general The Panel of Health Advisors (in this section referred to as the Panel ) shall be within the Congressional Budget Office. (b) Duties and priority target areas (1) Duties The Panel shall\u2014 (A) provide technical and functional expertise and recommendations to the Congressional Budget Office to improve the office\u2019s studies, analysis, and cost estimates related to health and health care issues and policies; (B) meet at least once annually; and (C) issue an annual report to the chair and ranking minority members of the Committee on the Budget of the House of Representatives and the Committee on the Budget of the Senate which\u2014 (i) details the work of the Panel and includes such recommendations as have been approved by a vote of at least 9 members of the Panel and provided to the Congressional Budget Office; and (ii) includes a description prepared by the Director of the Congressional Budget Office detailing how the office utilized any such recommendations provided under clause (i) and the extent to which any such recommendations were integrated into the office\u2019s studies and cost estimates. (2) Priority target areas For the purposes of this section, the Director of the Congressional Budget Office, in consultation with the chairs and ranking minority members of the Committee on the Budget of the House of Representatives and the Committee on the Budget of the Senate, as well as members on the Panel, shall determine priorities to address in meetings of the Panel, and the report detailed under paragraph (1)(C). The Panel shall provide expertise and recommendations under paragraph (1) with specific respect to the following areas: (A) Non-economic and economic studies on health and health care issues and policies developed by the Congressional Budget Office. (B) Official cost estimates prepared by the Congressional Budget Office for proposed health care legislation. (C) Models developed and utilized by the Congressional Budget Office to project non-economic and economic impacts of health care policy changes and legislation. (D) Health care components of the Congressional Budget Office\u2019s annual Budget and Economic Outlook publications, Federal Health Subsidies for Health Insurance reports, Health Insurance Coverage Projections, and other official publications related to health and health care by the Congressional Budget Office. (3) Publication The Director of the Congressional Budget Office shall publish, on the Office\u2019s public website, the annual report prepared pursuant to paragraph (1)(C). (4) Ethical disclosure; confidentiality The Director of the Congressional Budget Office may establish\u2014 (A) a system for public disclosure by members of the Panel related to potential conflicts of interest relating to such members; and (B) confidentiality agreements with members of the Panel to protect information obtained by the Government on a confidential basis to inform official work products and confidential congressional requests for analytical reports and budgetary scoring estimates. (c) Membership (1) Number and appointment The membership of the Panel shall include 15 members appointed not later than 90 days after the date of the enactment of this section, of which\u2014 (A) 3 members shall be appointed by the chair of the Committee on the Budget of the House of Representatives; (B) 3 members shall be appointed by the ranking minority member of the Committee on the Budget of the House of Representatives; (C) 3 members shall be appointed by the chair of the Committee on the Budget of the Senate; (D) 3 members shall be appointed by the ranking minority member of the Committee on the Budget of the Senate; and (E) 3 members shall be appointed by the Director of the Congressional Budget Office. (2) Qualifications The membership of the Panel shall aim to include, but not be limited to, individuals with national recognition for their expertise in health finance and economics, actuarial science, health facility management, life sciences and drug development, investment in health care companies, health plans and integrated delivery systems, reimbursement of health facilities, allopathic and osteopathic physicians, and other providers of health services, Medicare, Medicaid, and other related fields. (3) Special Government employees Members of the Panel shall serve as special Government employees (as defined in section 202(a) of title 18, United States Code). (d) Terms (1) In general The terms of the members of the Panel shall be for 3 years, except that the Director of the Congressional Budget Office shall designate staggered terms of the members first appointed. (2) Vacancies (A) In general A vacancy in the Panel shall be filled in the manner in which the original appointment was made. (B) Term of member appointed to fill vacancy Any member appointed to fill a vacancy occurring before the expiration of the term for which the member\u2019s predecessor was appointed shall be appointed only for the remainder of that term, except that a member may serve after the expiration of that member\u2019s term until a successor has taken office. (3) Chair; vice chair (A) In general The Director of the Congressional Budget Office shall designate a member of the Panel, at the time of appointment of the member, as chair and a member as vice chair for that term of appointment, except that in the case of vacancy of the chair or vice chair, the Director of the Congressional Budget Office may designate another member for the remainder of that member\u2019s term. (B) Requirements The chair and vice chair shall be appointed by the Director of the Congressional Budget Office\u2014 (i) after considering recommendations received from the chairs of the Committee on the Budget of the House of Representatives and the Committee on the Budget of the Senate ; (ii) without regard to political affiliation; and (iii) solely on the basis of their fitness to perform their duties. (4) Limits Members of the Panel shall be limited to two 3-year terms, for a total of not to exceed 6 years of service on the Panel. For purposes of this paragraph, any year of service on the Panel by a person appointed to fill a vacancy under paragraph (2) shall be included in determining the number of years that such person has served on the Panel. .\n##### (b) Clerical amendment\nThe table of contents of such Act is amended by inserting after the item relating to section 203 the following:\n204. Panel of Health Advisors. .",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on the Budget."
      },
      "number": "751",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HEALTH Panel Act",
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
            "name": "Advisory bodies",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Congressional Budget Office (CBO)",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-06-13T18:12:51Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-13T18:12:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-06-23T18:15:19Z"
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
          "measure-id": "id119s1911",
          "measure-number": "1911",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1911v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Healthy Equipping And Lending Technical Help Panel Act or the HEALTH Panel Act</strong></p><p>This bill provides statutory authority for the Panel of Health Advisors within the Congressional Budget Office (CBO). The panel provides expertise and recommendations to CBO to support\u00a0its analysis and cost estimates relating to health and healthcare.</p><p>The bill requires the panel to report to the House and Senate Budget Committees on the recommendations the panel provided to CBO and how CBO utilized such recommendations. CBO must publish this report on its website.</p><p>The bill also requires the panel to consist of 15 members serving three-year terms. The respective chairs and ranking minority members of the House and Senate Budget Committees, and the director of CBO, must\u00a0each appoint three members to the panel.</p>"
        },
        "title": "HEALTH Panel Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1911.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Healthy Equipping And Lending Technical Help Panel Act or the HEALTH Panel Act</strong></p><p>This bill provides statutory authority for the Panel of Health Advisors within the Congressional Budget Office (CBO). The panel provides expertise and recommendations to CBO to support\u00a0its analysis and cost estimates relating to health and healthcare.</p><p>The bill requires the panel to report to the House and Senate Budget Committees on the recommendations the panel provided to CBO and how CBO utilized such recommendations. CBO must publish this report on its website.</p><p>The bill also requires the panel to consist of 15 members serving three-year terms. The respective chairs and ranking minority members of the House and Senate Budget Committees, and the director of CBO, must\u00a0each appoint three members to the panel.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1911"
    },
    "title": "HEALTH Panel Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Healthy Equipping And Lending Technical Help Panel Act or the HEALTH Panel Act</strong></p><p>This bill provides statutory authority for the Panel of Health Advisors within the Congressional Budget Office (CBO). The panel provides expertise and recommendations to CBO to support\u00a0its analysis and cost estimates relating to health and healthcare.</p><p>The bill requires the panel to report to the House and Senate Budget Committees on the recommendations the panel provided to CBO and how CBO utilized such recommendations. CBO must publish this report on its website.</p><p>The bill also requires the panel to consist of 15 members serving three-year terms. The respective chairs and ranking minority members of the House and Senate Budget Committees, and the director of CBO, must\u00a0each appoint three members to the panel.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1911"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1911is.xml"
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
      "title": "HEALTH Panel Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HEALTH Panel Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Equipping And Lending Technical Help Panel Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Congressional Budget and Impoundment Control Act of 1974 to codify the Panel of Health Advisors within the Congressional Budget Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:29Z"
    }
  ]
}
```
