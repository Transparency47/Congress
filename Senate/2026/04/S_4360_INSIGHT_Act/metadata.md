# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4360?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4360
- Title: INSIGHT Act
- Congress: 119
- Bill type: S
- Bill number: 4360
- Origin chamber: Senate
- Introduced date: 2026-04-21
- Update date: 2026-05-13T19:03:07Z
- Update date including text: 2026-05-13T19:03:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in Senate
- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-21: Introduced in Senate

## Actions

- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4360",
    "number": "4360",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "INSIGHT Act",
    "type": "S",
    "updateDate": "2026-05-13T19:03:07Z",
    "updateDateIncludingText": "2026-05-13T19:03:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T19:34:10Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AL"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4360is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4360\nIN THE SENATE OF THE UNITED STATES\nApril 21, 2026 Mr. Banks (for himself, Mr. Cassidy , Mr. Tuberville , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to require that the Employee Benefit Security Administration make annual reports to Congress on investigations relating to enforcement and on adverse interest agreements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Investigation Status and Governance for Honest Transparency Act or the INSIGHT Act .\n#### 2. Annual report on investigations\nSection 504 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1134 ) is amended by adding at the end the following:\n(f) Report on investigations (1) In general Not later than December 31 of each year following the date of enactment of this subsection, the Secretary shall submit to Congress a report on the status of cases in enforcement status, including investigations that are active, or in relation to which the Secretary asserted investigative authority or engaged in targeted compliance monitoring, under subsection (a), during the preceding fiscal year. (2) Contents (A) In general The report required under paragraph (1) shall include the following information in relation to each investigation under subsection (a): (i) The regional or district office, or any other office, of the Employee Benefit Security Administration that opened the investigation. (ii) The date the investigation was opened. (iii) The date on which the Secretary first requested documents from the target of the investigation. (iv) In relation to the date on which the Secretary first requested documents from the target of the investigation in relation to such investigation\u2014 (I) whether the investigation was concluded within the 36-month period beginning on the date of such request; and (II) if such investigation has not been concluded by the end of such 36-month period\u2014 (aa) information on why such investigation has not been concluded; and (bb) the estimated date of conclusion. (B) Excluded information The report shall not include any information that identifies any private party to the investigation, including any plan, plan sponsor, fiduciary, service provider, employee, or participant or beneficiary. (C) Conclusion of investigations For the purposes of paragraph (A)(iv), an investigation shall not be considered concluded until the later of\u2014 (i) the date on which the Secretary ceases to assert investigative authority in relation to such investigation; or (ii) if applicable, terminates any targeted compliance monitoring, in each case as memorialized in a closing letter delivered to the target of the investigation or the party subject to compliance monitoring. In the event that the issues or topics under investigation change during the course of an investigation, the Secretary\u2019s continuing assertion of authority under this section shall be treated as a continuing investigation and not as a separate investigation. .\n#### 3. Report on adverse interest agreements\n##### (a) In general\nSection 504 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1134 ), as amended by section 2, is further amended by adding at the end the following:\n(g) Collaboration with plaintiff attorneys (1) In general In the event that the Secretary provides adverse assistance to an individual, prior to providing the adverse assistance, the Secretary shall\u2014 (A) enter into a written agreement with the individual that details the nature and scope of such assistance; and (B) provide a copy of such agreement to any employer, plan sponsor, or fiduciary that may be directly and adversely impacted by such assistance. (2) Adverse assistance defined For purposes of this subsection, the term adverse assistance means assistance or advice, including the disclosure of information as described in subsection (a), that is directed specifically toward an attorney for potential use in a civil action under section 502(a). (3) Report (A) In general Not later than 60 days after the date of enactment of this subsection, and by December 31 of each year that begins after such date, the Secretary shall submit to Congress a report containing information on all agreements to provide adverse assistance in effect for the preceding fiscal year, including, in relation to each such agreement\u2014 (i) a copy of the agreement, with any information described in subparagraph (B)(ii) redacted; (ii) the date the agreement was entered into; (iii) a detailed description of the nature and scope of the assistance provided during the fiscal year, including\u2014 (I) the information shared, including the source, type, and amount of the information, and the date on which such information was shared; (II) a log of verbal communications, including\u2014 (aa) the date of each communication; (bb) the parties engaged in such communication; (cc) the mode of communication; and (dd) the nature of any information shared; and (III) a log of meetings, including\u2014 (aa) the date of each meeting; (bb) the parties present at the meeting; (cc) mode of the meeting; and (dd) the purpose of such meeting and the nature of any information shared; and (iv) an explanation of how such agreement is consistent with the public policy of promoting the voluntary sponsorship of employee benefit plans subject to this Act. (B) Identifying information The report described under paragraph (A)\u2014 (i) shall identify the parties to each agreement; and (ii) may not include any information that may be used to identify any other person (including an employer, plan sponsor, plan fiduciary, service provider, or any other potential defendant). .\n##### (b) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall apply to any adverse assistance provided on or after the date of enactment of this Act.\n**(2) Existing agreements**\nFor the purposes of section 504(g)(1) of the Employee Retirement Income Security Act ( 29 U.S.C. 1134(f)(1) ) (as added by subsection (a)), if, not later than 60 days after the date of enactment of this Act, the Secretary of Labor takes the actions required in paragraphs (A) and (B) of such section 504(g)(1) in relation to an existing arrangement to provide adverse assistance, the Secretary shall be deemed to have taken such actions prior to providing such adverse assistance.\n#### 4. Private pension plans as integral to the continued well-being and security of employees and their dependents\nSection 2 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 ) is amended by adding at the end the following:\n(d) Congress finds that the retirement security of millions of employees and their dependents is directly impacted by the voluntary sponsorship and maintenance of pension plans. It is hereby declared to be a policy of this Act to promote, encourage, and facilitate the voluntary establishment and maintenance of, and contribution to, such plans. .",
      "versionDate": "2026-04-21",
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
        "actionDate": "2026-02-20",
        "text": "Placed on the Union Calendar, Calendar No. 430."
      },
      "number": "2958",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Balance the Scales Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-13T19:03:07Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4360is.xml"
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
      "title": "INSIGHT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INSIGHT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investigation Status and Governance for Honest Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to require that the Employee Benefit Security Administration make annual reports to Congress on investigations relating to enforcement and on adverse interest agreements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:34Z"
    }
  ]
}
```
