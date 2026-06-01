# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/305
- Title: One School, One Nurse Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 305
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-05-20T08:08:05Z
- Update date including text: 2026-05-20T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/305",
    "number": "305",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "One School, One Nurse Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:05Z",
    "updateDateIncludingText": "2026-05-20T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:37:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:37:30Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "TX"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr305ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 305\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Wilson of Florida introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the Secretary of Education to carry out a grant program to assist local educational agencies with ensuring that each elementary and secondary school has at least one registered nurse on staff.\n#### 1. Short title\nThis Act may be cited as the One School, One Nurse Act of 2025 .\n#### 2. Purpose; findings\n##### (a) Purpose\nThe purpose of this Act is to assist States and local educational agencies with ensuring that every elementary and secondary school has at least one full-time registered nurse on staff, and to maintain recommended nurse-to-student ratios, including through the recruitment, hiring, and retention of registered nurses.\n##### (b) Findings\nCongress finds the following:\n**(1)**\nAccording to the American Academy of Pediatrics, every elementary and secondary school should have at least one full-time registered nurse on staff.\n**(2)**\nAccording to the National Center for Education Statistics, during the 2015\u20132016 school year, only about half of all public schools had a full-time registered nurse and nearly 20 percent did not have any nurse on staff. Schools with higher free or reduced-price lunch program eligibility rates had lower rates of school nurses.\n**(3)**\nAccording to the Georgetown University Center for Children and Families, in 2019, roughly 6 percent of children in the United States were uninsured.\n**(4)**\nFor children who lack health care coverage, a school nurse is often a critical source of health services.\n**(5)**\nStudies suggest that schools with a full-time registered nurse experience far-reaching benefits including fewer student absences, students spending more time in class, more accurate medical records, higher immunization rates, fewer student pregnancies, and better health outcomes for students with asthma or diabetes.\n**(6)**\nSchool nurses play a critical role in helping to manage the chronic physical, emotional, mental, and social health needs of students, conduct health screenings, facilitate vaccinations and immunization compliance efforts, reduce burdens on educators and other school staff, and support a positive and healthy school climate.\n#### 3. One School, One Nurse grant program\n##### (a) Grant program authorized\nNot later than 12 months after the date of enactment of this section, the Secretary shall establish a program to award grants, on a competitive basis, to eligible entities to carry out the activities under subsection (d) . Grants awarded under this section shall be for a period of 5 years.\n##### (b) Application\nAn eligible entity desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require. Such application shall include\u2014\n**(1)**\na needs assessment of the eligible entity that demonstrates the existence of persistent shortages of school nurses or persistent shortages of full-time school nurses;\n**(2)**\na description of the health and wellness needs of the student population served by the eligible entity;\n**(3)**\na comprehensive plan for the use of grant funds to address persistent shortages described in the needs assessment under paragraph (1) , including a description of how such activities shall address the health and wellness needs described under paragraph (2) and how such funds will be used to ensure that the eligible entity will continue to employ and retain school nurses after the completion of the grant period; and\n**(4)**\na description of how the eligible entity will prioritize recruiting individuals from the communities served by the eligible entity and from underrepresented populations in public health professions (as determined by the Secretary by regulation), and how the eligible entity will track progress in meeting any specified hiring goals.\n##### (c) Selection and priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that\u2014\n**(1)**\nare a high-need local educational agency, or are a partnership between a State educational agency and a consortium of high-need local educational agencies; and\n**(2)**\ndescribe and set specific hiring goals towards increasing the share of school nurses who are from underrepresented populations in public health professions.\n##### (d) Activities\nGrant funds awarded under this section shall be used by an eligible entity to carry out one or more of the following activities:\n**(1)**\nRecruit and hire school nurses.\n**(2)**\nProvide resources necessary to convert part-time school nurse positions at elementary or secondary schools served by the eligible entity into full-time school nurse positions.\n**(3)**\nSupport the retention of school nurses, including by increasing salaries.\n**(4)**\nMaintain recommended nurse-to-student ratios (as determined by the Secretary by regulation).\n##### (e) Reporting\nEach eligible entity awarded a grant under this section shall submit to the Secretary an annual report for each year of the grant award. Such report shall include\u2014\n**(1)**\na summary of the eligible entity\u2019s progress in employing at least one full-time registered nurse at each elementary and secondary school served by the eligible entity and maintaining recommended nurse-to-student ratios (as determined by the Secretary by regulation);\n**(2)**\ndata on the number and percentage of full-time and part-time school nurses, disaggregated by major racial and ethnic groups and gender, employed at each elementary and secondary school served by the eligible entity; and\n**(3)**\na summary of any progress made by the eligible entity in addressing the health and wellness needs identified in the needs assessment required under subsection (b)(2) as a result of activities carried out with a grant under this section.\n##### (f) Regulations required\nNot later than 12 months after the date of enactment of this section, the Secretary shall\u2014\n**(1)**\nin consultation with the Secretary of Health and Human Services\u2014\n**(A)**\nspecify in regulation the recommended nurse-to-student ratios for elementary and secondary schools;\n**(B)**\nprovide for guidance and other technical assistance to eligible entities with respect to achieving and maintaining such ratios; and\n**(C)**\nspecify in regulation the definition of underrepresented populations in public health professions for the purposes of this section; and\n**(2)**\nin consultation with the Secretary of Health and Human Services and the Secretary of Labor, specify in regulation the definition of full-time with respect to school nurses for the purposes of this section.\n##### (g) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na local educational agency; or\n**(B)**\na partnership between a State educational agency and a consortium of local educational agencies in the State, entered into for the purposes of a grant under this section.\n**(2) High-need local educational agency**\nThe term high-need local educational agency has the meaning given such term in section 200 of the Higher Education Act of 1965 ( 20 U.S.C. 1021 ).\n**(3) Local educational agency; State educational agency**\nThe terms local educational agency and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) School nurse**\nThe term school nurse means a registered nurse who is employed by a school or local educational agency or State or State educational agency and is qualified under State law to provide assessment, diagnosis, counseling, educational, therapeutic, and other health services to meet student needs.\n**(5) Secretary**\nThe term Secretary means the Secretary of Education.",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Department of Education",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-02-12T19:17:45Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-12T19:17:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-06T19:50:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr305",
          "measure-number": "305",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr305v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>One School, One Nurse Act of </strong><strong>2025</strong></p><p>This bill directs the Department of Education (ED) to award competitive grants to eligible entities for recruiting, hiring, and retaining school nurses. An eligible entity is a local educational agency (LEA) or a partnership between a state educational agency and a consortium of LEAs in the state.</p><p>Further, ED must specify in regulation the recommended nurse-to-student ratios for elementary and secondary schools.</p>"
        },
        "title": "One School, One Nurse Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr305.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One School, One Nurse Act of </strong><strong>2025</strong></p><p>This bill directs the Department of Education (ED) to award competitive grants to eligible entities for recruiting, hiring, and retaining school nurses. An eligible entity is a local educational agency (LEA) or a partnership between a state educational agency and a consortium of LEAs in the state.</p><p>Further, ED must specify in regulation the recommended nurse-to-student ratios for elementary and secondary schools.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr305"
    },
    "title": "One School, One Nurse Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One School, One Nurse Act of </strong><strong>2025</strong></p><p>This bill directs the Department of Education (ED) to award competitive grants to eligible entities for recruiting, hiring, and retaining school nurses. An eligible entity is a local educational agency (LEA) or a partnership between a state educational agency and a consortium of LEAs in the state.</p><p>Further, ED must specify in regulation the recommended nurse-to-student ratios for elementary and secondary schools.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr305"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr305ih.xml"
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
      "title": "One School, One Nurse Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One School, One Nurse Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Education to carry out a grant program to assist local educational agencies with ensuring that each elementary and secondary school has at least one registered nurse on staff.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:31Z"
    }
  ]
}
```
