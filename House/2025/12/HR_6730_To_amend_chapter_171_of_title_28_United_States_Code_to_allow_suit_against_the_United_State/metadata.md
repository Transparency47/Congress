# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6730?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6730
- Title: HERO Act
- Congress: 119
- Bill type: HR
- Bill number: 6730
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-02-03T09:05:27Z
- Update date including text: 2026-02-03T09:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6730",
    "number": "6730",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "HERO Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:27Z",
    "updateDateIncludingText": "2026-02-03T09:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-16T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NC"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "MI"
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
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "HI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NV"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6730ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6730\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Issa (for himself, Mr. Hudson , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend chapter 171 of title 28, United States Code, to allow suit against the United States for injuries and deaths of members of the Armed Forces caused by improper medical care.\n#### 1. Short title\nThis Act may be cited as the Healthcare Equality and Rights for Our Heroes Act or the HERO Act .\n#### 2. Claims against United States for injury and death of members of the uniform services caused by improper medical care\n##### (a) Repeal\nSection 2733a of title 10, United States Code, is repealed.\n##### (b) In general\nChapter 171 of title 28, United States Code, is amended by adding at the end the following:\n2681. Claims against United States for injury and death of members of the uniformed services (a) Notwithstanding any other provision of law, a claim may be brought against the United States under this chapter for damages for personal injury or death of a member of the uniformed services arising out of a negligent or wrongful act or omission in the performance of medical, dental, or related health care functions (including clinical studies and investigations) that is provided at a covered military medical treatment facility by an employee acting within the scope of their office or employment or by or at the direction of the Government of the United States and shall be exclusive of any other civil action or proceeding by reason of the same subject matter against such employee (or the estate of such employee) whose act or omission gave rise to the action or proceeding. (b) A claim under this section may not be reduced\u2014 (1) by the amount of any benefit received pursuant to laws administered by the Secretary of Veterans Affairs; or (2) by the amount of any benefit received under subchapter III (relating to Servicemembers\u2019 Group Life Insurance) of chapter 19 of title 38. (c) Notwithstanding section 2401(b)\u2014 (1) except as provided in paragraph (2), a claim arising under this section may not be commenced later than 10 years after the date on which the claimant discovered, or by reasonable diligence should have discovered, the injury and the cause of the injury; and (2) with respect to an administrative claim pending pursuant to section 2733a of title 10 as of the enactment of this subsection, the limitations period described in paragraph (1) shall begin on the date of enactment of this subsection. (d) For purposes of claims brought under this section\u2014 (1) subsections (j) and (k) of section 2680 shall not apply; and (2) in the case of an act or omission occurring outside the United States, the law of the place where the act or omission occurred shall be deemed to be the law of the State of domicile of the claimant. (e) Not later than 2 years after the date of the enactment of this section, and every 2 years thereafter, the Attorney General shall submit to Congress a report on the number of claims filed under this section. (f) In this section\u2014 (1) the term active service has the meaning given such term in section 101 of title 10; (2) the term Armed Forces has the meaning given the term in section 101 of title 10; (3) the term covered military medical treatment facility \u2014 (A) means a facility maintained under section 1073d of title 10; and (B) does not include battalion aid stations or other military medical treatment facilities in an area of armed conflict or combatant activities. (4) the term member of the uniformed services includes a member of a reserve component of the Armed Forces if the claim by the member under this section is in connection with personal injury or death that occurred while the member was performing active service; (5) the term reserve components means the reserve components specified in section 10101 of title 10; and (6) the term uniformed services shall have the meaning given such term in section 101 of title 10. .\n##### (c) Clerical amendment\nThe table of sections for chapter 171 of title 28, United States Code, is amended by adding at the end the following:\n2681. Claims against United States for injury and death of members of the Armed Forces. .",
      "versionDate": "2025-12-16",
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
        "name": "Law",
        "updateDate": "2025-12-18T16:22:56Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6730ih.xml"
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
      "title": "HERO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HERO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Equality and Rights for Our Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 171 of title 28, United States Code, to allow suit against the United States for injuries and deaths of members of the Armed Forces caused by improper medical care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T09:18:39Z"
    }
  ]
}
```
