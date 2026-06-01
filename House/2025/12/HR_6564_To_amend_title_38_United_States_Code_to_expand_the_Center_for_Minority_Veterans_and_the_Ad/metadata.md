# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6564
- Title: Historically Underserved Veterans Inclusion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6564
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-09T09:07:08Z
- Update date including text: 2026-01-09T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6564",
    "number": "6564",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Historically Underserved Veterans Inclusion Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T09:07:08Z",
    "updateDateIncludingText": "2026-01-09T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:12:28Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "MA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NV"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6564ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6564\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mrs. Cherfilus-McCormick introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand the Center for Minority Veterans and the Advisory Committee on Minority Veterans to include services for historically underserved veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Historically Underserved Veterans Inclusion Act of 2025 .\n#### 2. Expansion of Center for Minority Veterans and Advisory Committee on Minority Veterans of the Department of Veterans Affairs\n##### (a) Center for Minority and Historically Underserved Veterans\nSection 317 of title 38, United States Code, is amended\u2014\n**(1)**\nin the heading, by inserting and Historically Underserved after Minority ;\n**(2)**\nby inserting Executive before Director each place it appears;\n**(3)**\nin subsection (a)\u2014\n**(A)**\nby inserting and Historically Underserved after Minority ; and\n**(B)**\nby striking the Center a and inserting the Center an ;\n**(4)**\nin subsection (d), by striking veterans who are minorities each place it appears and inserting covered veterans ; and\n**(5)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking veterans who are minorities means and inserting covered veterans ; and\n**(ii)**\nby inserting and veterans who are historically underserved after minority group members ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking The term and inserting The terms ;\n**(ii)**\nby inserting and veterans who are historically underserved after minority group member ;\n**(iii)**\nby striking has the meaning given such term and inserting have the meanings given such terms ; and\n**(iv)**\nby striking section 544(d) and inserting section 544 .\n##### (b) Advisory Committee on Minority and Historically Underserved Veterans\nSection 544 of title 38, United States Code, is amended\u2014\n**(1)**\nin the heading, by inserting and Historically Underserved after Minority ;\n**(2)**\nby striking veterans who are minority group members each place it appears and inserting covered veterans ;\n**(3)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting and Historically Underserved after Minority ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)(v)\u2014\n**(I)**\nby striking women ; and\n**(II)**\nby inserting who are women before and are ; and\n**(ii)**\nin subparagraph (B), by adding at the end the following new clauses:\n(vii) The Secretary of Housing and Urban Development (or a representative of the Secretary of Housing and Urban Development designated by the Secretary of Housing and Urban Development). (viii) The Secretary of Education (or a representative of the Secretary of Education designated by the Secretary of Education). (ix) The Attorney General (or a representative of the Attorney General designated by the Attorney General). (x) The Administrator of the Small Business Administration (or a representative of the Administrator of the Small Business Administration designated by the Administrator of the Small Business Administration). (xi) The Director of the Office of National Drug Control Policy (or a representative of the Director of the Office of National Drug Control Policy designated by the Director of the Office of National Drug Control Policy). ; and\n**(C)**\nby adding at the end the following new paragraph:\n(5) The duties of the Committee are to advise the Secretary on the following: (A) Modifying programs of the Department relating to policy, regulations, and legislative affairs to improve the representation of covered veterans within the Department. (B) Expanding benefits and services under the laws administered by the Secretary for covered veterans, including such benefits and services relating to health care, suicide prevention, and homelessness. (C) Incorporating research and practices from outreach programs to improve the provision of health care and burial benefits under the laws administered by the Secretary to covered veterans. (D) Addressing issues raised by State and local organizations that serve covered veterans. (E) Issuing, to private, non-profit, and faith-based organizations that serve covered veterans, guidance relating to addressing the needs of covered veterans. (F) Helping covered veterans receive benefits and services under the laws administered by the Secretary to which covered veterans are entitled. (G) Improving the methods by which covered veterans may submit feedback to the Department with respect to policies and regulations of the Secretary, including through stakeholder forums, social media, and virtual town halls. (H) Developing outreach and engagement to covered veterans. (I) Commemorating the contributions of covered veterans to their respective communities. (J) To explore options on how the Secretary may incorporate lessons learned utilizing journey mapping, human center design, social determinants of wellness metrics, or other means to illustrate the life experience cycle of minority and historically underserved veterans to create a more holistic understanding of important life cycle events and their impact. ;\n**(4)**\nby striking subsection (e);\n**(5)**\nby redesignating subsection (d) as subsection (e);\n**(6)**\nby inserting after subsection (c) the following new subsection:\n(d) (1) The Secretary shall, on a biennial basis, carry out a review to identify any disparities among groups of veterans in the receipt of benefits under the laws administered by the Secretary. In carrying out any such review, the Secretary shall consider relevant recommendations from the Committee and data analysis conducted by the Department. (2) Not later than 120 days after the date on which Secretary completes any such review, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes, if applicable, recommendations with respect to extending services of Center for Minority and Historically Underserved Veterans under section 517 of this title to groups of veterans the Secretary determines to be historically underserved pursuant to such review. ; and\n**(7)**\nin subsection (e) (as so redesignated)\u2014\n**(A)**\nby striking section, and all that follows through who is\u2014 and inserting section: ;\n**(B)**\nby redesignating paragraphs (1) through (5) as subparagraphs (A) through (E), respectively (and adjusting the margins accordingly);\n**(C)**\nby inserting before subparagraph (A) (as so redesignated) the following new paragraphs:\n(1) The term covered veterans means veterans who are minority group members and veterans who are historically underserved. (2) The term minority group member means an individual who is\u2014 ;\n**(D)**\nin paragraph (2) (as added by subparagraph (C))\u2014\n**(i)**\nin subparagraph (D) (as so redesignated), by striking or ;\n**(ii)**\nin subparagraph (E) (as so redesignated), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end of the following new subparagraphs:\n(F) Middle Eastern or North African American; or (G) identified with more than one race or ethnicity described in subparagraphs (A) through (F). ; and\n**(E)**\nby adding after paragraph (2) (as added by subparagraph (D)) the following new paragraph:\n(3) The term veterans who are historically underserved means veterans the Committee determines have experienced difficulty in receiving benefits under the laws administered by the Secretary to which such veterans are entitled on the basis of one or more of the following: (A) Sexual orientation. (B) Gender identity. (C) English language proficiency. (D) United States citizenship. (E) Religion. (F) Low socioeconomic status. (G) Residing in a rural community (as defined in regulations promulgated by the Secretary of Agriculture). (H) Membership in a group of veterans the Secretary determines appropriate pursuant to the biennial review required under subsection (d). .\n#### 3. Reinstatement of Department of Veterans Affairs Office of Equity Assurance; biannual briefing\n##### (a) Reinstatement\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\npermanently reinstate the authority, functions, responsibilities, and research activities of the Office of Equity Assurance of the Veterans Benefits Administration;\n**(2)**\nreinstate the employment of each employee of the Office of Equity Assurance, if such employee was terminated after January 20, 2025;\n**(3)**\nensure that a position in the Office of Equity Assurance may not be eliminated pursuant to a reduction in force; and\n**(4)**\nprovide to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a briefing with respect to the status of the implementation of recommendations included in the report of the Comptroller General of the United States titled VA Disability Benefits: Action Needed to Further Examine Racial and Ethnic Disparities in Compensation (GAO\u201323\u2013106097; published July 26, 2023).\n##### (b) Biannual briefing\nNot later than 30 days after the date on which the Secretary reinstates the Office of Equity Assurance pursuant to subsection (a), and on a biannual basis thereafter, the Under Secretary of Veterans Affairs for Benefits shall provide to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a briefing on the data, research, and analysis developed by the Office of Equity Assurance during the period covered by the briefing.",
      "versionDate": "2025-12-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:51:42Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6564ih.xml"
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
      "title": "Historically Underserved Veterans Inclusion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Historically Underserved Veterans Inclusion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand the Center for Minority Veterans and the Advisory Committee on Minority Veterans to include services for historically underserved veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T04:48:26Z"
    }
  ]
}
```
