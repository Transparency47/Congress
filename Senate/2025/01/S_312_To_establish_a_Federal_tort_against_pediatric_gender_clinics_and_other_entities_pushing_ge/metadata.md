# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/312?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/312
- Title: Jamie Reed Protecting Our Kids from Child Abuse Act
- Congress: 119
- Bill type: S
- Bill number: 312
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-02-26T00:26:17Z
- Update date including text: 2026-02-26T00:26:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/312",
    "number": "312",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Jamie Reed Protecting Our Kids from Child Abuse Act",
    "type": "S",
    "updateDate": "2026-02-26T00:26:17Z",
    "updateDateIncludingText": "2026-02-26T00:26:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T20:40:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s312is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 312\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Hawley (for himself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a Federal tort against pediatric gender clinics and other entities pushing gender-transition procedures that cause bodily injury to children or harm the mental health of children.\n#### 1. Short title\nThis Act may be cited as the Jamie Reed Protecting Our Kids from Child Abuse Act .\n#### 2. Federal tort for harm to children caused by gender-transition procedures\n##### (a) Definitions\nIn this section:\n**(1) Gender transition procedure**\n**(A) In general**\nExcept as provided in subparagraph (B), the term gender-transition procedure means\u2014\n**(i)**\nthe prescription or administration of gonadotropin-releasing hormone agonists or any other puberty-blocking drugs for the purpose of changing the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual's biological sex of male or female;\n**(ii)**\nthe prescription or administration of testosterone (when prescribed to a female) or estrogen (when prescribed to a male) for the purpose of changing the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual\u2019s biological sex of male or female; or\n**(iii)**\na surgery to change the body of an individual so that it conforms to the subjective sense of identity of the individual, in the case such identity is at odds with the individual\u2019s biological sex of male or female.\n**(B) Exception**\nThe term gender-transition procedure does not include\u2014\n**(i)**\nan intervention described in subparagraph (A) that is performed on\u2014\n**(I)**\nan individual with biological sex characteristics that are inherently ambiguous, such as those born with 46 XX chromosomes with virilization, 46 XY chromosomes with undervirilization, or having both ovarian and testicular tissue; or\n**(II)**\nan individual with respect to whom a physician has determined through genetic or biochemical testing that the individual does not have normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action, for a biological male or biological female;\n**(ii)**\nthe treatment of any infection, injury, disease, or disorder that has been caused or exacerbated by the performance of an intervention described in subparagraph (A) without regard to whether the intervention was performed in accordance with State or Federal law or whether the intervention is covered by the private right of action under subsection (c); or\n**(iii)**\nany procedure undertaken because the individual suffers from a physical disorder, physical injury, or physical illness that would, as certified by a physician, place the individual in imminent danger of death or impairment of major bodily function unless the procedure is performed.\n**(2) Hospital**\nThe term hospital has the meaning given such term in section 1861(e) of the Social Security Act ( 42 U.S.C. 1395x(e) ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Medical practitioner**\nThe term medical practitioner means a person who is licensed, certified, or otherwise authorized by the laws of a State to administer health care in the ordinary course of the practice of the person\u2019s profession.\n**(5) Minor**\nThe term minor means an individual who has not yet reached 18 years of age.\n**(6) Pediatric gender clinic**\nThe term pediatric gender clinic means a medical facility that specializes in the diagnosis or treatment of gender discordance and gender dysphoria in minors, including medical interventions such as therapeutic diagnosis of gender dysphoria and performance of (or referral for) gender-transition procedures on minors.\n##### (b) Liability\nThe following individuals and entities shall be liable in accordance with this section to any individual who suffers bodily injury or harm to mental health (including any physical, psychological, emotional, or physiological harm) that is attributable, in whole or in part, to a gender-transition procedure performed on the individual when the individual was a minor:\n**(1)**\nA pediatric gender clinic where the gender-transition procedure was provided.\n**(2)**\nAny medical practitioner who administered health care, at the time of the particular procedure, at the pediatric gender clinic where the gender-transition procedure was provided.\n**(3)**\nAn institution of higher education that hosts, operates, partners with, provides funding to, or is otherwise affiliated with the pediatric gender clinic where the gender-transition procedure was provided.\n**(4)**\nA hospital that hosts, operates, partners with, provides funding to, or is otherwise affiliated with the pediatric gender clinic where the gender-transition procedure was provided.\n**(5)**\nAny medical practitioner who performed the gender-transition procedure on the individual.\n##### (c) Private right of action\nAn individual who suffers bodily injury or harm to mental health that is attributable, in whole or in part, to a gender-transition procedure provided to the individual when the individual was a minor may, not later than 30 years after the date on which the individual turns 18 years of age, bring a civil action against an individual or entity described in subsection (b), in an appropriate district court of the United States or a State court of competent jurisdiction for\u2014\n**(1)**\ncompensatory damages;\n**(2)**\npunitive damages; and\n**(3)**\nattorney\u2019s fees and costs.\n##### (d) Affirmative defense\nIt shall be an affirmative defense to an action brought by or on behalf of an individual upon whom a gender-transition procedure was performed under subsection (c) that the pediatric gender clinic or medical practitioner who performed the gender-transition procedure on the individual, at all relevant times, did not know and had no reason to know that the individual in question was a minor.\n#### 3. Prohibition on funding\nNo Federal funds may be made available\u2014\n**(1)**\nto a pediatric gender clinic;\n**(2)**\nto an institution of higher education or hospital that hosts, operates, partners with, provides funding to, or is otherwise affiliated with, a pediatric gender clinic; or\n**(3)**\nfor any gender-transition procedure performed on a minor.\n#### 4. Effective date and retroactive application\nThis Act shall\u2014\n**(1)**\ntake effect on the date of enactment of this Act; and\n**(2)**\napply to any gender-transition procedure that took place before, on, or after the effective date under paragraph (1).\n#### 5. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the remaining provisions of this Act, to any person or circumstance, shall not be affected.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Energy and Commerce, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4618",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Jamie Reed Protecting Our Kids from Child Abuse Act",
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
            "name": "Child health",
            "updateDate": "2025-04-04T16:01:28Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-04T16:02:27Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-04-04T16:02:11Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-04-04T16:01:46Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-04T16:02:35Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-04T16:02:50Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-04T16:02:44Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-04T16:01:54Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-04-04T16:01:34Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2025-04-04T16:02:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T15:05:20Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s312is.xml"
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
      "title": "Jamie Reed Protecting Our Kids from Child Abuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Jamie Reed Protecting Our Kids from Child Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Federal tort against pediatric gender clinics and other entities pushing gender-transition procedures that cause bodily injury to children or harm the mental health of children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:04:03Z"
    }
  ]
}
```
