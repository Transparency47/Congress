# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6034
- Title: VET Extension Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6034
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-05T17:01:01Z
- Update date including text: 2025-12-05T17:01:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-20 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6034",
    "number": "6034",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "VET Extension Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T17:01:01Z",
    "updateDateIncludingText": "2025-12-05T17:01:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:32:39Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6034ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6034\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Horsford introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide additional entitlement to Post-9/11 Educational Assistance to certain veterans and members of the Armed Forces who require extra time to complete remedial and deficiency courses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Education and Transfer Extension Act of 2025 or the VET Extension Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nIndividuals who are entitled to educational assistance under the Post-9/11 Educational Assistance program of the Department of Veterans Affairs who require remedial and deficiency courses exhaust their entitlement before completing a program of education with such assistance.\n**(2)**\nMembers of the Armed Forces who are entitled to educational assistance under such program and who do not have dependents while serving as members of the Armed Forces are not able to transfer their entitlement to such assistance when they come to have dependents.\n#### 3. Increase in duration of educational assistance under Department of Veterans Affairs Post-9/11 Educational Assistance program for completion of remedial and deficiency courses\n##### (a) In general\nSection 3312 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) Increase for pursuit of remedial and deficiency courses (1) In general In the case of an individual who is eligible under paragraph (2), the number of months of educational assistance under section 3313 of this title to which the individual is entitled under this section is increased by the lesser of the following: (A) 15 months. (B) The number of months required to complete the remedial and deficiency courses necessary to complete the program of education the individual is pursuing on a full-time basis, as determined by the Secretary. (2) Eligibility For purposes of this section, an eligible individual is an individual who\u2014 (A) was entitled to educational assistance under section 3311 of this title but has used all of such individual\u2019s entitlement; (B) during the 180-day period preceding the date of the determination of eligibility under this subsection, used any of such entitlement; and (C) is pursuing the completion of a program of education at an institution of higher learning and\u2014 (i) has completed, or attempted to complete, a remedial or deficiency course necessary to complete such program of education; and (ii) requires more than the standard 120 semester (or 180 quarter) credit hours for completion of such program of education. (3) Definitions In this subsection: (A) The term institution of higher learning has the meaning given such term in section 3452 of this title. (B) The term remedial or deficiency course means a course offered by an institution of higher learning that is designed to overcome a deficiency. .\n##### (b) Conforming amendments\nTitle 38, United States Code, is further amended\u2014\n**(1)**\nin section 3312(a), by striking subsections (b) and (c) and inserting subsections (b), (c), and (d) ; and\n**(2)**\nin section 3695, by adding at the end the following new subsection:\n(d) Notwithstanding subsection (a), in the case of an individual who is entitled to additional months of educational assistance under section 3312(d) of this title, the aggregate period for which such individual may receive assistance under two or more of the provisions of law referred to in such subsection may not exceed the sum of\u2014 (1) 48 months (or the part-time equivalent thereof), and (2) the number of months of entitlement received by such individual under section 3312(d) of this title. .\n#### 4. Increased flexibility in transfer of entitlement to educational assistance under Department of Veterans Affairs Post-9/11 Educational Assistance program\nSection 3319 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and indenting such subparagraphs appropriately;\n**(B)**\nin the matter before subparagraph (A), as redesignated by subparagraph (A), by striking An and inserting the following:\n(1) In general An ; and\n**(C)**\nby adding at the end the following new paragraph (2):\n(2) Timing of designation An individual who does not have an eligible dependent may elect to transfer a portion of the individual\u2019s entitlement to an unspecified future dependent. In the case of such an election, the individual shall make the designations required by paragraph (1) when the individual comes to have an eligible dependent to whom the individual would like to transfer entitlement under this section. ; and\n**(2)**\nin subsection (f)\u2014\n**(A)**\nby striking paragraph (1);\n**(B)**\nby redesignating paragraphs (2) and (3) as paragraphs (1) and (2), respectively; and\n**(C)**\nin paragraph (1)(A), as redesignated by subparagraph (B), by inserting , including by designating a new dependent or dependents to whom to transfer the individual\u2019s entitlement before the period.",
      "versionDate": "2025-11-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T17:01:01Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6034ih.xml"
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
      "title": "VET Extension Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VET Extension Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Education and Transfer Extension Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide additional entitlement to Post-9/11 Educational Assistance to certain veterans and members of the Armed Forces who require extra time to complete remedial and deficiency courses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T03:18:22Z"
    }
  ]
}
```
