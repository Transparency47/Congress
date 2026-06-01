# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1493
- Title: To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1493
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-05-23T08:07:35Z
- Update date including text: 2026-05-23T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 43 - 0.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 43 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1493",
    "number": "1493",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000034",
        "district": "6",
        "firstName": "Frank",
        "fullName": "Rep. Pallone, Frank [D-NJ-6]",
        "lastName": "Pallone",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:35Z",
    "updateDateIncludingText": "2026-05-23T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 43 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
        "item": [
          {
            "date": "2026-05-21T13:46:56Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-21T20:34:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NE"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1493ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1493\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Pallone (for himself, Mr. Bacon , Mr. Menendez , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes.\n#### 1. Programs to prevent, detect, and treat traumatic brain injuries\n##### (a) The Bill Pascrell, Jr., national program for traumatic brain injury surveillance and registries\n**(1) Prevention of traumatic brain injury**\nSection 393B of the Public Health Service Act ( 42 U.S.C. 280b\u20131c ) is amended\u2014\n**(A)**\nin subsection (a), by inserting and prevalence after incidence ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by inserting and reduction of associated injuries and fatalities before the semicolon;\n**(ii)**\nin paragraph (2), by inserting and related risk factors before the semicolon; and\n**(iii)**\nin paragraph (3)\u2014\n**(I)**\nin the matter preceding subparagraph (A), by striking 2020 each place it appears and inserting 2030 ; and\n**(II)**\nin subparagraph (A)\u2014\n**(aa)**\nin clause (i), by striking ; and and inserting of traumatic brain injury; ;\n**(bb)**\nby redesignating clause (ii) as clause (iv);\n**(cc)**\nby inserting after clause (i) the following:\n(ii) populations at higher risk of traumatic brain injury, including populations whose increased risk is due to occupational or circumstantial factors; (iii) causes of, and risk factors for, traumatic brain injury; and ; and\n**(dd)**\nin clause (iv), as so redesignated, by striking arising from traumatic brain injury and inserting , which may include related mental health and other conditions, arising from traumatic brain injury, including ; and\n**(C)**\nin subsection (c), by inserting , and other relevant Federal departments and agencies before the period at the end.\n**(2) National program for traumatic brain injury surveillance and registries**\nSection 393C of the Public Health Service Act ( 42 U.S.C. 280b\u20131d ) is amended\u2014\n**(A)**\nby amending the section heading to read as follows: The Bill Pascrell, Jr., national program for traumatic brain injury surveillance and registries ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nin the matter preceding paragraph (1), by inserting to identify populations that may be at higher risk for traumatic brain injuries, to collect data on the causes of, and risk factors for, traumatic brain injuries, after related disability, ;\n**(ii)**\nin paragraph (1), by inserting , including the occupation of the individual, when relevant to the circumstances surrounding the injury before the semicolon; and\n**(iii)**\nin paragraph (4), by inserting short- and long-term before outcomes ;\n**(C)**\nby striking subsection (b);\n**(D)**\nby redesignating subsection (c) as subsection (b);\n**(E)**\nin subsection (b), as so redesignated, by inserting and evidence-based practices to identify and address concussion before the period at the end; and\n**(F)**\nby adding at the end the following:\n(c) Availability of information The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall make publicly available aggregated information on traumatic brain injury and concussion described in this section, including on the website of the Centers for Disease Control and Prevention. Such website, to the extent feasible, shall include aggregated information on populations that may be at higher risk for traumatic brain injuries and strategies for preventing or reducing risk of traumatic brain injury that are tailored to such populations. .\n**(3) Authorization of appropriations**\nSection 394A of the Public Health Service Act ( 42 U.S.C. 280b\u20133 ) is amended\u2014\n**(A)**\nin subsection (a), by striking 1994, and and inserting 1994, ; and\n**(B)**\nin subsection (b), by striking 2020 through 2024 and inserting 2026 through 2030 .\n##### (b) State grant programs\n**(1) State grants for projects regarding traumatic brain injury**\nSection 1252 of the Public Health Service Act ( 42 U.S.C. 300d\u201352 ) is amended\u2014\n**(A)**\nin subsection (b)(2)\u2014\n**(i)**\nby inserting , taking into consideration populations that may be at higher risk for traumatic brain injuries after outreach programs ; and\n**(ii)**\nby inserting Tribal, after State, ;\n**(B)**\nin subsection (c), by adding at the end the following:\n(3) Maintenance of effort With respect to activities for which a grant awarded under subsection (a) is to be expended, a State or American Indian consortium shall agree to maintain expenditures of non-Federal amounts for such activities at a level that is not less than the level of such expenditures maintained by the State or American Indian consortium for the fiscal year preceding the fiscal year for which the State or American Indian consortium receives such a grant. (4) Waiver The Secretary may, upon the request of a State or American Indian consortium, waive not more than 50 percent of the matching fund amount under paragraph (1), if the Secretary determines that such matching fund amount would result in an inability of the State or American Indian consortium to carry out the purposes under subsection (a). A waiver provided by the Secretary under this paragraph shall apply only to the fiscal year involved. ;\n**(C)**\nin subsection (e)(3)(B)\u2014\n**(i)**\nby striking (such as third party payers, State agencies, community-based providers, schools, and educators) ; and\n**(ii)**\nby inserting (such as third party payers, State agencies, community-based providers, schools, and educators) after professionals ;\n**(D)**\nin subsection (h), by striking paragraphs (1) and (2) and inserting the following:\n(1) American Indian consortium; State The terms American Indian consortium and State have the meanings given such terms in section 1253. (2) Traumatic brain injury (A) In general Subject to subparagraph (B), the term traumatic brain injury \u2014 (i) means an acquired injury to the brain; (ii) may include\u2014 (I) brain injuries caused by anoxia due to trauma; and (II) damage to the brain from an internal or external source that results in infection, toxicity, surgery, or vascular disorders not associated with aging; and (iii) does not include brain dysfunction caused by congenital or degenerative disorders, or birth trauma. (B) Revisions to definition The Secretary may revise the definition of the term traumatic brain injury under this paragraph, as the Secretary determines necessary, after consultation with States and other appropriate public or nonprofit private entities. ; and\n**(E)**\nin subsection (i), by striking 2020 through 2024 and inserting 2026 through 2030 .\n**(2) State grants for protection and advocacy services**\nSection 1253(l) of the Public Health Service Act ( 42 U.S.C. 300d\u201353(l) ) is amended by striking 2020 through 2024 and inserting 2026 through 2030 .\n##### (c) Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that contains\u2014\n**(1)**\nan overview of populations who may be at higher risk for traumatic brain injury, such as individuals affected by domestic violence or sexual assault and public safety officers as defined in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 );\n**(2)**\nan outline of existing surveys and activities of the Centers for Disease Control and Prevention on traumatic brain injuries and any steps the agency has taken to address gaps in data collection related to such higher risk populations, which may include leveraging surveys such as the National Intimate Partner and Sexual Violence Survey to collect data on traumatic brain injuries;\n**(3)**\nan overview of any outreach or education efforts to reach such higher risk populations; and\n**(4)**\nany challenges associated with reaching such higher risk populations.\n##### (d) Study on long-Term symptoms or conditions related to traumatic brain injury\n**(1) In general**\nThe Secretary, in consultation with stakeholders and the heads of other relevant Federal departments and agencies, as appropriate, shall conduct, either directly or through a contract with a nonprofit private entity, a study to\u2014\n**(A)**\nexamine the incidence and prevalence of long-term or chronic symptoms or conditions in individuals who have experienced a traumatic brain injury;\n**(B)**\nexamine the evidence base of research related to the chronic effects of traumatic brain injury across the lifespan;\n**(C)**\nexamine any correlations between traumatic brain injury and increased risk of other conditions, such as dementia and mental health conditions;\n**(D)**\nassess existing services available for individuals with such long-term or chronic symptoms or conditions; and\n**(E)**\nidentify any gaps in research related to such long-term or chronic symptoms or conditions of individuals who have experienced a traumatic brain injury.\n**(2) Public report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall\u2014\n**(A)**\nsubmit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report detailing the findings, conclusions, and recommendations of the study described in paragraph (1); and\n**(B)**\nin the case that such study is conducted directly by the Secretary, make the report described in subparagraph (A) publicly available on the website of the Department of Health and Human Services.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T17:30:12Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:17:38Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T17:28:56Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T17:30:19Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-17T17:28:18Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-17T17:28:32Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-17T17:30:05Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-07-17T17:27:58Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-17T17:29:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T14:39:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1493",
          "measure-number": "1493",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1493v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill reauthorizes from FY2026-FY2030 and expands Department of Health and Human Services (HHS) programs relating to traumatic brain injuries. It also requires HHS to conduct a study and report to Congress on traumatic brain injuries.</p><p>Specifically, the bill reauthorizes</p><ul><li>Centers for Disease Control and Prevention (CDC) grants to states for traumatic brain injury surveillance and registries (renaming the program after the late Representative\u00a0Bill Pascrell, Jr.),\u00a0</li><li>CDC research and public awareness activities to reduce traumatic brain injuries,</li><li>Administration for Community Living (ACL) grants to states and American Indian consortiums for services and support for individuals living with traumatic brain injuries, and</li><li>ACL grants for protection and advocacy agencies supporting individuals with traumatic brain injuries.</li></ul><p>Also, the bill generally expands the scope and requirements of these programs, including by requiring the CDC to publish information on populations at higher risk for traumatic brain injuries and strategies for preventing such injuries in these populations.\u00a0</p><p>Additionally, HHS must conduct a study on long-term symptoms or conditions in people who experience traumatic brain injuries and report the findings to Congress. HHS must also submit a report to Congress on populations with a higher risk of traumatic brain injuries and outreach efforts for such populations.</p>"
        },
        "title": "To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1493.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill reauthorizes from FY2026-FY2030 and expands Department of Health and Human Services (HHS) programs relating to traumatic brain injuries. It also requires HHS to conduct a study and report to Congress on traumatic brain injuries.</p><p>Specifically, the bill reauthorizes</p><ul><li>Centers for Disease Control and Prevention (CDC) grants to states for traumatic brain injury surveillance and registries (renaming the program after the late Representative\u00a0Bill Pascrell, Jr.),\u00a0</li><li>CDC research and public awareness activities to reduce traumatic brain injuries,</li><li>Administration for Community Living (ACL) grants to states and American Indian consortiums for services and support for individuals living with traumatic brain injuries, and</li><li>ACL grants for protection and advocacy agencies supporting individuals with traumatic brain injuries.</li></ul><p>Also, the bill generally expands the scope and requirements of these programs, including by requiring the CDC to publish information on populations at higher risk for traumatic brain injuries and strategies for preventing such injuries in these populations.\u00a0</p><p>Additionally, HHS must conduct a study on long-term symptoms or conditions in people who experience traumatic brain injuries and report the findings to Congress. HHS must also submit a report to Congress on populations with a higher risk of traumatic brain injuries and outreach efforts for such populations.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr1493"
    },
    "title": "To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill reauthorizes from FY2026-FY2030 and expands Department of Health and Human Services (HHS) programs relating to traumatic brain injuries. It also requires HHS to conduct a study and report to Congress on traumatic brain injuries.</p><p>Specifically, the bill reauthorizes</p><ul><li>Centers for Disease Control and Prevention (CDC) grants to states for traumatic brain injury surveillance and registries (renaming the program after the late Representative\u00a0Bill Pascrell, Jr.),\u00a0</li><li>CDC research and public awareness activities to reduce traumatic brain injuries,</li><li>Administration for Community Living (ACL) grants to states and American Indian consortiums for services and support for individuals living with traumatic brain injuries, and</li><li>ACL grants for protection and advocacy agencies supporting individuals with traumatic brain injuries.</li></ul><p>Also, the bill generally expands the scope and requirements of these programs, including by requiring the CDC to publish information on populations at higher risk for traumatic brain injuries and strategies for preventing such injuries in these populations.\u00a0</p><p>Additionally, HHS must conduct a study on long-term symptoms or conditions in people who experience traumatic brain injuries and report the findings to Congress. HHS must also submit a report to Congress on populations with a higher risk of traumatic brain injuries and outreach efforts for such populations.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr1493"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1493ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:03:26Z"
    },
    {
      "title": "To reauthorize and make improvements to Federal programs relating to the prevention, detection, and treatment of traumatic brain injuries, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:05:51Z"
    }
  ]
}
```
