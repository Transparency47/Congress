# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4166?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4166
- Title: SECURE Grid Act
- Congress: 119
- Bill type: S
- Bill number: 4166
- Origin chamber: Senate
- Introduced date: 2026-03-24
- Update date: 2026-05-19T23:07:23Z
- Update date including text: 2026-05-19T23:07:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in Senate
- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-24: Introduced in Senate

## Actions

- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4166",
    "number": "4166",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "SECURE Grid Act",
    "type": "S",
    "updateDate": "2026-05-19T23:07:23Z",
    "updateDateIncludingText": "2026-05-19T23:07:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:29:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "AK"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4166is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4166\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2026 Ms. Cortez Masto (for herself, Ms. Murkowski , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy Policy and Conservation Act to require States to include supporting the physical security, cybersecurity, and resilience of local distribution systems in State energy security plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Community Upgrades for a Resilient Grid Act or the SECURE Grid Act .\n#### 2. Consideration of the security of local distribution systems in State energy security plans\nSection 366 of the Energy Policy and Conservation Act ( 42 U.S.C. 6326 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraph (2) as paragraph (3); and\n**(B)**\nby inserting after paragraph (1) the following:\n(2) Local distribution system The term local distribution system means any energy infrastructure owned and operated by an electric utility at a voltage of 100 kilovolts or less. ;\n**(2)**\nin subsection (b)(2), in the matter preceding subparagraph (A), by inserting , and suppliers of equipment for the generation, transmission, and distribution of electricity to, after owners and operators of ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking paragraph (3) and inserting the following:\n(3) address potential hazards to each energy sector or system, including\u2014 (A) physical threats and vulnerabilities, including\u2014 (i) weather-related threats and vulnerabilities; (ii) physical attacks on local distribution systems and the bulk-power system; and (iii) supply chain risks for equipment for the generation, transmission, and distribution of electricity; and (B) cybersecurity threats and vulnerabilities, including threats to, and vulnerabilities of, local distribution systems that may impact the bulk-power system; ; and\n**(B)**\nby striking paragraph (5) and inserting the following:\n(5) provide a risk mitigation approach to enhance reliability and end-use resilience, including methods of responding to, mitigating, and recovering from potential hazards described in paragraph (3); and ;\n**(4)**\nin subsection (d)(3)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) supplying equipment for the generation, transmission, and distribution of electricity; and ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting appropriately;\n**(B)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and indenting appropriately;\n**(C)**\nin the matter preceding subparagraph (A) (as so designated), by striking A State is not eligible and inserting the following:\n(1) Submission required A State is not eligible ; and\n**(D)**\nby adding at the end the following:\n(2) State determination A submission under paragraph (1) is not required to be approved by the Secretary. ;\n**(6)**\nin subsection (f), by striking may and inserting shall ;\n**(7)**\nin subsection (h), in the matter preceding paragraph (1), by inserting , local distribution system, after electric utility ; and\n**(8)**\nby striking subsection (i) and inserting the following:\n(i) Sunset This section shall expire on September 30, 2031. .\n#### 3. GAO report\n##### (a) Definition of State energy security plan\nIn this section, the term State energy security plan has the meaning given the term in section 366(a) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(a) ).\n##### (b) Report\nNot later than September 30, 2030, the Comptroller General of the United States shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report on the efficacy of State energy security plans that includes\u2014\n**(1)**\nan evaluation of whether and how State energy security plans have improved the ability of States\u2014\n**(A)**\nto identify, assess, and mitigate risks to energy infrastructure and supply chains; and\n**(B)**\nto plan for, respond to, and recover from events that disrupt energy supply;\n**(2)**\nrecommendations for\u2014\n**(A)**\nimproving the ability of States described in paragraph (1); and\n**(B)**\nactions the Secretary of Energy may take to improve coordination with States with respect to identifying, assessing, and mitigating risks to energy infrastructure and supply chains and planning for, responding to, and recovering from events that disrupt energy supply;\n**(3)**\ninformation on Federal financial assistance made available to States under part D of title III of the Energy Policy and Conservation Act ( 42 U.S.C. 6321 et seq. ) that was used to implement State energy security plans;\n**(4)**\ninformation on activities carried out by States using that financial assistance;\n**(5)**\nan analysis of the efficacy of the implementation of section 366 of the Energy Policy and Conservation Act ( 42 U.S.C. 6326 ) (as amended by this Act); and\n**(6)**\ninformation on State use of assistance provided under section 366(f) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(f) ) (as amended by this Act), including any revisions of State energy security plans made by States resulting from assistance provided under that section.\n##### (c) Protected information\nThe report required under subsection (b) shall be submitted in a form that may be made available to the public, except that any information protected from disclosure under section 366(h) of the Energy Policy and Conservation Act ( 42 U.S.C. 6326(h) ) shall be included in the report in an annex that shall not be publicly disclosed, consistent with that section.",
      "versionDate": "2026-03-24",
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
        "actionDate": "2026-05-11",
        "text": "Placed on the Union Calendar, Calendar No. 561."
      },
      "number": "7257",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SECURE Grid Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-04-03T21:43:39Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4166is.xml"
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
      "title": "SECURE Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SECURE Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Community Upgrades for a Resilient Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Policy and Conservation Act to require States to include supporting the physical security, cybersecurity, and resilience of local distribution systems in State energy security plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:27Z"
    }
  ]
}
```
