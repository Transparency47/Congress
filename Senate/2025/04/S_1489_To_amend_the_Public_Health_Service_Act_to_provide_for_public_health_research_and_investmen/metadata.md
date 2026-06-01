# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1489
- Title: Anti-Racism in Public Health Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1489
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-10T16:14:01Z
- Update date including text: 2026-04-10T16:14:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-09-02 - Floor: Star Print ordered on the measure.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-09-02 - Floor: Star Print ordered on the measure.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1489",
    "number": "1489",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Anti-Racism in Public Health Act of 2025",
    "type": "S",
    "updateDate": "2026-04-10T16:14:01Z",
    "updateDateIncludingText": "2026-04-10T16:14:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the measure.",
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
          "date": "2025-04-11T02:30:27Z",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1489is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1489\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Warren (for herself, Mr. Markey , Mr. Merkley , Ms. Smith , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to provide for public health research and investment into understanding and eliminating structural racism and police violence.\n#### 1. Short title\nThis Act may be cited as the Anti-Racism in Public Health Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Antiracism**\nThe term antiracism is a collection of antiracist policies that lead to racial equity, and are substantiated by antiracist ideas.\n**(2) Antiracist**\nThe term antiracist is any measure that produces or sustains racial equity between racial groups.\n#### 3. Public health research and investment in dismantling structural racism\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by adding at the end the following:\n320C. National Center on Antiracism and Health (a) In general (1) National center There is established within the Centers for Disease Control and Prevention a center to be known as the National Center on Antiracism and Health (referred to in this section as the Center ). The Director of the Centers for Disease Control and Prevention shall appoint a director to head the Center who has experience living in and working with racial and ethnic minority communities. The Center shall promote public health by\u2014 (A) declaring racism a public health crisis and naming racism as an historical and present threat to the physical and mental health and well-being of the United States and world; (B) aiming to develop new knowledge in the science and practice of antiracism, including by identifying the mechanisms by which racism operates in the provision of health care and in systems that impact health and well-being; (C) transferring that knowledge into practice, including by developing interventions that dismantle the mechanisms of racism and replace such mechanisms with equitable structures, policies, practices, norms, and values so that a healthy society can be realized; and (D) contributing to a national and global conversation regarding the impacts of racism on the health and well-being of the United States and world. (2) General duties The Secretary, acting through the Center, shall undertake activities to carry out the mission of the Center as described in paragraph (1), such as the following: (A) Conduct research into, collect, analyze and make publicly available data on, and provide leadership and coordination for the science and practice of antiracism, the public health impacts of structural racism, and the effectiveness of intervention strategies to address these impacts. Topics of research and data collection under this subparagraph may include identifying and understanding\u2014 (i) policies and practices that have a disparate impact on the health and well-being of communities of color; (ii) the public health impacts of implicit racial bias, White supremacy, weathering, xenophobia, discrimination, and prejudice; (iii) the social determinants of health resulting from structural racism, including poverty, housing, employment, political participation, and environmental factors; and (iv) the intersection of racism and other systems of oppression, including as related to age, sexual orientation, gender identity, and disability status. (B) Award noncompetitive grants and cooperative agreements to eligible public and nonprofit private entities, including State, local, territorial, and Tribal health agencies and organizations, for the research and collection, analysis, and reporting of data on the topics described in subparagraph (A). (C) Establish, through grants or cooperative agreements, at least 3 regional centers of excellence, located in racial and ethnic minority communities, in antiracism for the purpose of developing new knowledge in the science and practice of antiracism in health by researching, understanding, and identifying the mechanisms by which racism operates in the health space, racial and ethnic inequities in health care access and outcomes, the history of successful antiracist movements in health, and other antiracist public health work. (D) Establish a clearinghouse within the Centers for Disease Control and Prevention for the collection and storage of data generated under the programs implemented under this section for which there is not an otherwise existing surveillance system at the Centers for Disease Control and Prevention. Such data shall\u2014 (i) be comprehensive and disaggregated, to the extent practicable, by including racial, ethnic, primary language, sex, gender identity, sexual orientation, age, socioeconomic status, and disability disparities; (ii) be made publicly available; (iii) protect the privacy of individuals whose information is included in such data; and (iv) comply with privacy protections under the regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996. (E) Provide information and education to the public on the public health impacts of structural racism and on antiracist public health interventions. (F) Consult with other Centers and National Institutes within the Centers for Disease Control and Prevention, including the Office of Minority Health and Health Equity and the Center for State, Tribal, Local, and Territorial Support, to ensure that scientific and programmatic activities initiated by the agency consider structural racism in their designs, conceptualizations, and executions, which shall include\u2014 (i) putting measures of racism in population-based surveys; (ii) establishing a Federal Advisory Committee on racism and health for the Centers for Disease Control and Prevention; (iii) developing training programs, curricula, and seminars for the purposes of training public health professionals and researchers around issues of race, racism, and antiracism; (iv) providing standards and best practices for programming and grant recipient compliance with Federal data collection standards, including section 4302 of the Patient Protection and Affordable Care Act; and (v) establishing leadership and stakeholder councils with experts and leaders in racism and public health disparities. (G) Coordinate with the Indian Health Service and with the Centers for Disease Control and Prevention\u2019s Tribal Advisory Committee to ensure meaningful Tribal consultation, the gathering of information from Tribal authorities, and respect for Tribal data sovereignty. (H) Engage in government to government consultation with Indian Tribes and Tribal organizations. (I) At least every 2 years, produce and publicly post on the Centers for Disease Control and Prevention\u2019s website a report on antiracist activities completed by the Center, which may include newly identified antiracist public health practices. (b) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to carry out this section. .\n#### 4. Public health research and investment in police violence\n##### (a) In general\nThe Secretary of Health and Human Services shall establish within the National Center for Injury Prevention and Control of the Centers for Disease Control and Prevention (referred to in this section as the Center ) a law enforcement violence prevention program.\n##### (b) General duties\nIn implementing the program under subsection (a), the Center shall conduct research into, and provide leadership and coordination for\u2014\n**(1)**\nthe understanding and promotion of knowledge about the public health impacts of uses of force by law enforcement, including police brutality and violence;\n**(2)**\ndeveloping public health interventions and perspectives for eliminating deaths, injury, trauma, and negative mental health effects from police presence and interactions, including police brutality and violence; and\n**(3)**\nensuring comprehensive data collection, analysis, and reporting regarding police violence and misconduct in consultation with the Department of Justice and independent researchers.\n##### (c) Functions\nUnder the program under subsection (a), the Center shall\u2014\n**(1)**\nsummarize and enhance the knowledge of the distribution, status, and characteristics of law enforcement-related death, trauma, and injury;\n**(2)**\nconduct research and prepare, with the assistance of State public health departments\u2014\n**(A)**\nstatistics on law enforcement-related death, injury, and brutality;\n**(B)**\nstudies of the factors, including legal, socioeconomic, discrimination, and other factors that correlate with or influence police brutality;\n**(C)**\npublic information about uses of force by law enforcement, including police brutality and violence, for the practical use of the public health community, including publications that synthesize information relevant to the national goal of understanding police violence and methods for its control;\n**(D)**\ninformation to identify socioeconomic groups, communities, and geographic areas in need of study, and a strategic plan for research necessary to comprehend the extent and nature of police uses of force by law enforcement, including police brutality and violence, and determine what options exist to reduce or eradicate death and injury that result; and\n**(E)**\nbest practices in police violence prevention in other countries;\n**(3)**\naward grants, contracts, and cooperative agreements to provide for the conduct of epidemiologic research on uses of force by law enforcement, including police brutality and violence, by Federal, State, local, and private agencies, institutions, organizations, and individuals;\n**(4)**\naward grants, contracts, and cooperative agreements to community groups, independent research organizations, academic institutions, and other entities to support, execute, or conduct research on interventions to reduce or eliminate uses of force by law enforcement, including police brutality and violence;\n**(5)**\ncoordinate with the Department of Justice, and other Federal, State, and local agencies on the standardization of data collection, storage, and retrieval necessary to collect, evaluate, analyze, and disseminate information about the extent and nature of uses of force by law enforcement, including police brutality and violence, as well as options for the eradication of such practices;\n**(6)**\nsubmit an annual report to Congress on research findings with recommendations to improve data collection and standardization and to disrupt processes in policing that preserve and reinforce racism and racial disparities in public health;\n**(7)**\nconduct primary research and explore uses of force by law enforcement, including police brutality and violence, and options for its control; and\n**(8)**\nstudy alternatives to law enforcement response as a method of reducing police violence.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated, such sums as may be necessary to carry out this section.",
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
      "number": "2884",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Anti-Racism in Public Health Act of 2025",
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
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Age discrimination",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Centers for Disease Control and Prevention (CDC)",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:14:01Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Housing discrimination",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-09-03T15:11:50Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-09-03T15:11:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-20T13:40:39Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1489is.xml"
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
      "title": "Anti-Racism in Public Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Anti-Racism in Public Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to provide for public health research and investment into understanding and eliminating structural racism and police violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:46Z"
    }
  ]
}
```
