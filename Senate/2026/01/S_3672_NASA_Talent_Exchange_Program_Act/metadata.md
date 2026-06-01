# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3672?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3672
- Title: NASA Talent Exchange Program Act
- Congress: 119
- Bill type: S
- Bill number: 3672
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-02-11T17:45:26Z
- Update date including text: 2026-02-11T17:45:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3672",
    "number": "3672",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "NASA Talent Exchange Program Act",
    "type": "S",
    "updateDate": "2026-02-11T17:45:26Z",
    "updateDateIncludingText": "2026-02-11T17:45:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T19:23:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "MS"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3672is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3672\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Kim (for himself, Mr. Wicker , Mr. Padilla , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 51, United States Code, to authorize the Administrator of the National Aeronautics and Space Administration to conduct a public-private talent program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NASA Talent Exchange Program Act .\n#### 2. National Aeronautics and Space Administration public-private talent program\nSection 20113 of title 51, United States Code, is amended by adding at the end the following new subsection:\n(o) Public-Private talent program (1) Assignment authority (A) In general Subject to subparagraph (B), the Administrator may arrange for the temporary assignment of\u2014 (i) an employee of the Administration to a private sector entity; or (ii) an employee of a private sector entity to the Administration. (B) Agreement and consent The Administrator may only arrange for an assignment under subparagraph (A) if the Administrator has obtained\u2014 (i) the agreement of the private sector entity concerned; and (ii) the consent of the employee concerned. (2) Agreements (A) In general The Administrator shall provide for a written agreement among the Administrator, the private sector entity concerned, and the employee concerned regarding the terms and conditions of the assignment of an employee under this subsection. (B) Elements An agreement under subparagraph (A) shall\u2014 (i) in the case of an employee of the Administration\u2014 (I) require the employee, upon completion of the assignment, to serve in the Administration (or elsewhere in the civil service of the Federal Government if approved by the Administrator) for a period equal to twice the length of the period during which the employee was assigned to the private sector entity; and (II) contain language prohibiting the employee from improperly using predecisional or draft deliberative information that the employee may be privy to or aware of with respect to Administration programing, budgeting, resourcing, acquisition, or procurement for the benefit or advantage of the private sector entity to which the employee is assigned; and (ii) provide that if the employee of the Administration or of the private sector entity, as applicable, fails to comply with the terms of the agreement, such employee shall be liable to the United States for payment of all expenses of the assignment, unless such failure is for good and sufficient reason, as determined by the Administrator. (C) Treatment of liability for expenses (i) In general Any amount for which an employee is liable under subparagraph (B)(ii) shall be treated as a debt due the United States. (ii) Waiver The Administrator may waive, in whole or in part, collection of a debt described in clause (i) based on a determination that collection of the debt would be against equity and good conscience and not in the best interests of the United States, after taking into account any indication of fraud, misrepresentation, fault, or lack of good faith on the part of the employee concerned. (3) Termination An assignment under this subsection may, at any time and for any reason, be terminated by the Administration or the private sector entity concerned, as applicable. (4) Duration (A) In general An assignment under this subsection shall be\u2014 (i) for a period not less than 90 days and not more than 2 years; and (ii) subject to subparagraph (B), renewable for a period not more than 2 years. (B) Extension A renewal of an assignment under this subsection may be for a period more than 2 years, but not more than 4 years total, if the Administrator determines that the assignment is necessary to meet critical mission or program requirements. (5) Status of Federal employees assigned to private sector entities (A) In general An employee of the Administration who is assigned to a private sector entity under this subsection shall be considered, during the period of such assignment, to be on detail to a regular work assignment within the Administration for all purposes. The written agreement under paragraph (2) with respect to such employee shall address the specific terms and conditions related to the continued status of the employee as a Federal employee. (B) Certification In establishing a temporary assignment of an employee of the Administration to a private sector entity under this subsection, the Administrator shall\u2014 (i) certify that such assignment shall not have an adverse or negative impact on mission attainment or organizational capabilities associated with such assignment; and (ii) ensure that the normal duties and functions of such employee\u2014 (I) can be reasonably performed by other employees of the Administration without the permanent transfer or reassignment of other personnel of the Administration; and (II) are not, as a result of and during the course of such temporary assignment, performed or augmented by contractor personnel in violation of section 1710 of title 41. (6) Terms and conditions for private sector employees An employee of a private sector entity who is assigned to the Administration under this subsection\u2014 (A) shall continue to receive pay and benefits from the private sector entity from which such employee is assigned; (B) except as provided in subparagraph (C), shall not receive pay or benefits from the Administration; (C) shall be considered to be an employee of the Administration for purposes of\u2014 (i) chapters 73 and 81 of title 5; (ii) sections 201, 203, 205, 207, 208, 209, 603, 606, 607, 643, 654, 1905, and 1913 of title 18, except that such section 209 shall not apply to any salary, or contribution or supplementation of salary, made under subparagraph (A); (iii) sections 1343, 1344, and 1349(b) of title 31; (iv) chapter 171 of title 28, United States Code (commonly known as the Federal Tort Claims Act ) and any other Federal tort liability law; and (v) chapter 21 of title 41; (D) shall not have access to any trade secrets or any other nonpublic information that is of commercial value to the private sector entity from which such employee is assigned; (E) may not perform work that is considered inherently governmental in nature; and (F) may not be used to circumvent any limitation or restriction on the size of the workforce of the Administration. (7) Conflicts of interest The Administrator shall implement a system to identify, mitigate, and manage any conflict of interests that may arise as a result of the assignment of an employee under this subsection. (8) Prohibition against charging certain costs to the Federal Government A private sector entity may not charge the Administration or any other agency of the Federal Government, as direct or indirect costs under a Federal contract, the costs of pay or benefits paid by the entity to an employee assigned to the Administration under this subsection for the period of the assignment concerned. (9) Considerations In carrying out this subsection, the Administrator shall take into consideration\u2014 (A) the manner in which assignments under this subsection may best meet the needs of the Administration with respect to the training of employees; and (B) as applicable, areas of particular private sector expertise, such as cybersecurity. (10) Annual report (A) In general Not later than 180 days after the date of the enactment of this subsection, and not later than April 30 each year thereafter, the Administrator shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report summarizing the implementation of this subsection. (B) Elements Each report required by subparagraph (A) shall include, for the preceding fiscal year, the following: (i) The total number of employees of private sector entities assigned to the Administration. (ii) The total number of employees of the Administration assigned to private sector entities. (iii) A brief description and assessment of the talent management benefits as a result of such assignments, including\u2014 (I) an identification of the private sector entities to and from which employees were assigned; (II) a complete listing of the positions such employees were assigned to and from; (III) an identification of assigned roles and objectives of such assignments; (IV) the duration of each such assignment; (V) the pay grades and levels of each such assignment; and (VI) a description of any identified strategic human capital or operational challenge of such assignments. (11) Regulations Not later than 30 days after the date of the enactment of this subsection, the Administrator shall promulgate regulations to carry out this subsection. .",
      "versionDate": "2026-01-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-11T17:45:25Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3672is.xml"
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
      "title": "NASA Talent Exchange Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NASA Talent Exchange Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 51, United States Code, to authorize the Administrator of the National Aeronautics and Space Administration to conduct a public-private talent program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:26Z"
    }
  ]
}
```
