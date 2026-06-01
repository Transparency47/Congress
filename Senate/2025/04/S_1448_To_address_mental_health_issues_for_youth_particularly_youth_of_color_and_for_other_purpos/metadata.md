# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1448
- Title: Pursuing Equity in Mental Health Act
- Congress: 119
- Bill type: S
- Bill number: 1448
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T21:36:35Z
- Update date including text: 2025-12-05T21:36:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-05-08 - Floor: Star Print ordered on the bill.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-05-08 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1448",
    "number": "1448",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Pursuing Equity in Mental Health Act",
    "type": "S",
    "updateDate": "2025-12-05T21:36:35Z",
    "updateDateIncludingText": "2025-12-05T21:36:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T18:08:04Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NJ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1448is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1448\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Hirono (for herself, Mr. Blumenthal , Ms. Smith , Ms. Warren , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo address mental health issues for youth, particularly youth of color, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pursuing Equity in Mental Health Act .\n#### 2. Primary and Behavioral Health Care grant program\nSection 520K of the Public Health Service Act ( 42 U.S.C. 290bb\u201342 ) is amended\u2014\n**(1)**\nby redesignating subsections (d) through (i) as subsections (e) through (j), respectively;\n**(2)**\nby inserting after subsection (c) the following:\n(d) Special consideration regarding services for racial and ethnic minority groups In awarding grants under subsection (b), the Secretary may, as appropriate, give special consideration to eligible entities serving a high proportion of racial and ethnic minority groups. ;\n**(3)**\nin subsection (c)(2)(G), by striking subsection (e) and inserting subsection (f) ;\n**(4)**\nin subsection (i) (as redesignated by paragraph (1))\u2014\n**(A)**\nby striking subsection (f) and inserting subsection (g) ; and\n**(B)**\nby striking subsection (d)(2) and inserting subsection (e)(2) ; and\n**(5)**\nin subsection (j)(1) (as redesignated by paragraph (1)), by striking $60,000,000 for each of fiscal years 2023 through 2027 and inserting $60,000,000 for fiscal year 2025 and $80,000,000 for each of fiscal years 2026 through 2031 .\n#### 3. Addressing racial and ethnic minority mental health disparities research gaps\nNot later than 9 months after the date of enactment of this Act, the Director of the National Institutes of Health, in consultation with the Director of the National Institute of Mental Health, the Director of the National Institute on Minority Health and Health Disparities, and the Assistant Secretary for Mental Health and Substance Use, shall enter into an arrangement with the National Academies of Sciences, Engineering, and Medicine (or, if the National Academies of Sciences, Engineering, and Medicine decline to enter into such an arrangement, the Patient-Centered Outcomes Research Institute or another appropriate entity)\u2014\n**(1)**\nto conduct a study with respect to mental health disparities research gaps in racial and ethnic minority groups (as defined in section 1707(g) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g) )); and\n**(2)**\nto submit to Congress a report on the results of such study, including\u2014\n**(A)**\na compilation of information on the prevalence of mental health outcomes in such racial and ethnic minority groups;\n**(B)**\nan assessment of information on the impact of exposure to community violence, adverse childhood experiences, structural bias, and other psychological traumas on mental health outcomes in such racial and minority groups; and\n**(C)**\na selection of potential recommendations that can remedy the research gap in such racial and ethnic minority groups.\nIf no arrangement can be made with an entity specified in the previous sentence, the Agency for Healthcare Research and Quality shall conduct the study and submit the report, as described in paragraphs (1) and (2).\n#### 4. Health professions competencies to address racial and ethnic minority mental health disparities\nSection 597 of the Public Health Service Act ( 42 U.S.C. 290ll ) is amended\u2014\n**(1)**\nby redesignating subsections (b) and (c) as subsections (c) and (d), respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Best practices; core competencies An individual receiving a fellowship under subsection (a), or an entity selected by the Assistant Secretary to administer the program under this section, may use amounts awarded under this section to engage in the following activities related to the development and dissemination of best practices or core competencies addressing mental health disparities among racial and ethnic minority groups for use in the training of students in the professions of social work, psychology, psychiatry, addiction medicine, marriage and family therapy, mental health counseling, and substance misuse counseling: (1) Formation of committees or working groups comprised of experts from accredited health professions schools to identify best practices and core competencies relating to mental health disparities among racial and ethnic minority groups. (2) Planning of workshops in national fora to allow for public input into the educational needs associated with mental health disparities among racial and ethnic minority groups. (3) Dissemination and promotion of the use of best practices or core competencies in undergraduate and graduate health professions training programs nationwide. (4) Establishing external advisory boards to provide meaningful input into policy and program development and best practices to reduce mental health disparities among racial and ethnic minority groups. ; and\n**(3)**\nin subsection (d) (as so redesignated), by striking 2027 and inserting 2031 .\n#### 5. Racial and ethnic minority behavioral and mental health outreach and education strategy\nPart D of title V of the Public Health Service Act ( 42 U.S.C. 290dd et seq. ) is amended by inserting after section 553 ( 42 U.S.C. 290ee\u201310 ) of such Act the following:\n554. Behavioral and mental health outreach and education strategy (a) In general The Secretary shall, in consultation with advocacy and behavioral and mental health organizations serving racial and ethnic minority groups, develop and implement an outreach and education strategy to promote behavioral and mental health and reduce stigma associated with mental health conditions and substance use among racial and ethnic minority groups. Such strategy shall\u2014 (1) be designed to\u2014 (A) meet the diverse cultural and language needs of the various racial and ethnic minority groups; and (B) be developmentally and age-appropriate; (2) increase awareness of symptoms of mental illnesses common among such groups, taking into account differences within at-risk subgroups; (3) provide information on evidence-based, culturally and linguistically appropriate and adapted interventions and treatments; (4) ensure full participation of, and engage, both individuals receiving behavioral and mental health services and other community members, which may include adolescents and young adults, in the development and implementation of materials; and (5) seek to broaden the perspective among both individuals in racial and ethnic minority groups and communities serving such groups to use a comprehensive and integrated public health approach to promoting behavioral health by focusing on the intersection between behavioral and physical health. (b) Reports Beginning not later than 1 year after the date of the enactment of this section, and annually thereafter for 5 years, the Secretary shall submit to Congress, and make publicly available, a report on the extent to which the strategy developed and implemented under subsection (a) addressed behavioral and mental health outcomes associated with mental health conditions and substance use among racial and ethnic minority groups. (c) Definition In this section, the term racial and ethnic minority group has the meaning given to that term in section 1707(g). (d) Authorization of appropriations There is authorized to be appropriated to carry out this section $20,000,000 for each of fiscal years 2026 through 2031. .\n#### 6. Additional funds for National Institutes of Health\n##### (a) In general\nIn addition to amounts otherwise authorized to be appropriated to the National Institutes of Health, there is authorized to be appropriated to such Institutes $150,000,000 for each of fiscal years 2026 through 2031 to\u2014\n**(1)**\nbuild relations with communities and conduct or support clinical research, including clinical research on racial or ethnic disparities in physical and mental health; and\n**(2)**\nto carry out the Strategic Framework For Addressing Youth Mental Health Disparities developed by the National Institute of Mental Health.\n##### (b) Definition\nIn this section, the term clinical research has the meaning given to such term in section 409 of the Public Health Service Act ( 42 U.S.C. 284d ).\n#### 7. Additional funds for National Institute on Minority Health and Health Disparities\nIn addition to amounts otherwise authorized to be appropriated to the National Institute on Minority Health and Health Disparities, there is authorized to be appropriated to such Institute $750,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2904",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pursuing Equity in Mental Health Act",
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
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2025-05-20T19:02:01Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-05-20T19:02:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-20T13:48:21Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1448is.xml"
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
      "title": "Pursuing Equity in Mental Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pursuing Equity in Mental Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address mental health issues for youth, particularly youth of color, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:35Z"
    }
  ]
}
```
