# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2898
- Title: Dennis John Benigno Traumatic Brain Injury Program Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2898
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-04-09T15:43:58Z
- Update date including text: 2026-04-09T15:43:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-10-08 - Floor: Star Print ordered on the bill.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-10-08 - Floor: Star Print ordered on the bill.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2898",
    "number": "2898",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Dennis John Benigno Traumatic Brain Injury Program Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-09T15:43:58Z",
    "updateDateIncludingText": "2026-04-09T15:43:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
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
        "item": {
          "date": "2025-09-18T20:39:52Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2898is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2898\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Mullin (for himself, Mr. Kim , Mr. Cornyn , Mr. Padilla , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the Traumatic Brain Injury program.\n#### 1. Short title\nThis Act may be cited as the Dennis John Benigno Traumatic Brain Injury Program Reauthorization Act of 2025 .\n#### 2. The Bill Pascrell, Jr., national program for traumatic brain injury surveillance and registries\n##### (a) Prevention of traumatic brain injury\nSection 393B of the Public Health Service Act ( 42 U.S.C. 280b\u20131c ) is amended\u2014\n**(1)**\nin subsection (a), by inserting and prevalence after incidence ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting and reduction of associated injuries and fatalities before the semicolon;\n**(B)**\nin paragraph (2), by inserting and related risk factors before the semicolon; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking 2020 each place it appears and inserting 2030 ; and\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(II)**\nby redesignating clause (ii) as clause (iv);\n**(III)**\nby inserting after clause (i) the following:\n(ii) populations at higher risk of traumatic brain injury, including populations whose increased risk is due to occupational or circumstantial factors; (iii) causes of, and risk factors for, traumatic brain injury; and ; and\n**(IV)**\nin clause (iv), as so redesignated, by striking arising from traumatic brain injury and inserting , which may include related mental health and other conditions, arising from traumatic brain injury, including ; and\n**(3)**\nin subsection (c), by inserting , and other relevant Federal departments and agencies before the period at the end.\n##### (b) National program for traumatic brain injury surveillance and registries\nSection 393C of the Public Health Service Act ( 42 U.S.C. 280b\u20131d ) is amended\u2014\n**(1)**\nby amending the section heading to read as follows: The Bill Pascrell, Jr., national program for traumatic brain injury surveillance and registries ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting to identify populations that may be at higher risk for traumatic brain injuries, to collect data on the causes of, and risk factors for, traumatic brain injuries, after related disability, ;\n**(B)**\nin paragraph (1), by inserting , including the occupation of the individual, when relevant to the circumstances surrounding the injury before the semicolon; and\n**(C)**\nin paragraph (4), by inserting short- and long-term before outcomes ;\n**(3)**\nby striking subsection (b);\n**(4)**\nby redesignating subsection (c) as subsection (b);\n**(5)**\nin subsection (b), as so redesignated, by inserting and evidence-based practices to identify and address concussion before the period at the end; and\n**(6)**\nby adding at the end the following:\n(c) Availability of information The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall make publicly available aggregated information on traumatic brain injury and concussion described in this section, including on the website of the Centers for Disease Control and Prevention. Such website, to the extent feasible, shall include aggregated information on populations that may be at higher risk for traumatic brain injuries and strategies for preventing or reducing risk of traumatic brain injury that are tailored to such populations. .\n##### (c) Authorization of appropriations\nSection 394A of the Public Health Service Act ( 42 U.S.C. 280b\u20133 ) is amended\u2014\n**(1)**\nin subsection (a), by striking 1994, and and inserting 1994, ; and\n**(2)**\nin subsection (b), by striking 2020 through 2024 and inserting 2026 through 2030 .\n#### 3. State grant programs\n##### (a) State grants for projects regarding traumatic brain injury\nSection 1252 of the Public Health Service Act ( 42 U.S.C. 300d\u201352 ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nby inserting , taking into consideration populations that may be at higher risk for traumatic brain injuries after outreach programs ; and\n**(B)**\nby inserting Tribal, after State, ;\n**(2)**\nin subsection (c), by adding at the end the following:\n(3) Maintenance of effort With respect to activities for which a grant awarded under subsection (a) is to be expended, a State or American Indian consortium shall agree to maintain expenditures of non-Federal amounts for such activities at a level that is not less than the level of such expenditures maintained by the State or American Indian consortium for the fiscal year preceding the fiscal year for which the State or American Indian consortium receives such a grant. (4) Waiver The Secretary may, upon the request of a State or American Indian consortium, waive not more than 50 percent of the matching fund amount under paragraph (1), if the Secretary determines that such matching fund amount would result in an inability of the State or American Indian consortium to carry out the purposes under subsection (a). A waiver provided by the Secretary under this paragraph shall apply only to the fiscal year involved. ;\n**(3)**\nin subsection (e)(3)(B)\u2014\n**(A)**\nby striking (such as third party payers, State agencies, community-based providers, schools, and educators) ; and\n**(B)**\nby inserting (such as third party payers, State agencies, community-based providers, schools, and educators) after professionals ;\n**(4)**\nin subsection (h), by striking paragraphs (1) and (2) and inserting the following:\n(1) American Indian consortium; State The terms American Indian consortium and State have the meanings given such terms in section 1253. (2) Traumatic brain injury (A) In general Subject to subparagraph (B), the term traumatic brain injury \u2014 (i) means an acquired injury to the brain; (ii) may include\u2014 (I) brain injuries caused by anoxia due to trauma; and (II) damage to the brain from an internal or external source that results in infection, toxicity, surgery, or vascular disorders not associated with aging; and (iii) does not include brain dysfunction caused by congenital or degenerative disorders, or birth trauma. (B) Revisions to definition The Secretary may revise the definition of the term traumatic brain injury under this paragraph, as the Secretary determines necessary, after consultation with States and other appropriate public or nonprofit private entities. ; and\n**(5)**\nin subsection (i), by striking 2020 through 2024 and inserting 2026 through 2030 .\n##### (b) State grants for protection and advocacy services\nSection 1253(l) of the Public Health Service Act ( 42 U.S.C. 300d\u201353(l) ) is amended by striking 2020 through 2024 and inserting 2026 through 2030 .\n#### 4. Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that contains\u2014\n**(1)**\nan overview of populations who may be at higher risk for traumatic brain injury, such as individuals affected by domestic violence or sexual assault and public safety officers, as defined in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 );\n**(2)**\nan outline of existing surveys and activities of the Centers for Disease Control and Prevention on traumatic brain injuries and any steps the agency has taken to address gaps in data collection related to such higher risk populations, which may include leveraging surveys such as the National Intimate Partner and Sexual Violence Survey to collect data on traumatic brain injuries;\n**(3)**\nan overview of any outreach or education efforts to reach such higher risk populations; and\n**(4)**\nany challenges associated with reaching such higher risk populations.\n#### 5. Study on long-term symptoms or conditions related to traumatic brain injury\n##### (a) In general\nThe Secretary, in consultation with stakeholders and the heads of other relevant Federal departments and agencies, as appropriate, shall conduct, either directly or through a contract with a nonprofit private entity, a study to\u2014\n**(1)**\nexamine the incidence and prevalence of long-term or chronic symptoms or conditions in individuals who have experienced a traumatic brain injury;\n**(2)**\nexamine the evidence base of research related to the chronic effects of traumatic brain injury across the lifespan;\n**(3)**\nexamine any correlations between traumatic brain injury and increased risk of other conditions, such as dementia and mental health conditions;\n**(4)**\nassess existing services available for individuals with such long-term or chronic symptoms or conditions; and\n**(5)**\nidentify any gaps in research related to such long-term or chronic symptoms or conditions of individuals who have experienced a traumatic brain injury.\n##### (b) Public report\nNot later than 2 years after the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\nsubmit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report detailing the findings, conclusions, and recommendations of the study described in subsection (a); and\n**(2)**\nin the case that such study is conducted directly by the Secretary, make the report described in paragraph (1) publicly available on the website of the Department of Health and Human Services.",
      "versionDate": "2025-09-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-17T19:33:08Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:43:58Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-17T19:32:55Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-17T19:33:13Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-12-17T19:32:45Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-12-17T19:33:00Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-12-17T19:32:49Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-17T19:33:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-12-15T20:15:22Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2898is.xml"
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
      "title": "Dennis John Benigno Traumatic Brain Injury Program Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dennis John Benigno Traumatic Brain Injury Program Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Traumatic Brain Injury program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:28Z"
    }
  ]
}
```
