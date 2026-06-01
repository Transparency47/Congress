# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3492
- Title: Essential Caregivers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3492
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3492",
    "number": "3492",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Essential Caregivers Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
        "item": [
          {
            "date": "2025-12-16T19:29:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-16T19:29:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "MT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "NC"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "ND"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "RI"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "AR"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "AZ"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "RI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "ME"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MA"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NM"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AK"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3492is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3492\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Blumenthal (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to require skilled nursing facilities, nursing facilities, intermediate care facilities for the intellectually disabled, and inpatient rehabilitation facilities to permit essential caregivers access during any period in which regular visitation is restricted.\n#### 1. Short title\nThis Act may be cited as the Essential Caregivers Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the National Center for Health Statistics of the Centers for Disease Control and Prevention, an estimated 1,300,000 individuals resided in nursing homes in 2020 at the onset of the COVID\u201319 pandemic, and nearly half of all nursing home residents were living with a diagnosis of Alzheimer\u2019s or other related dementia.\n**(2)**\nRegulations issued pursuant to subtitle C of title IV of the Omnibus Budget Reconciliation Act of 1987 (commonly known as the Nursing Home Reform Act of 1987 ) ( Public Law 100\u2013203 ) established basic rights and services for residents of nursing homes, including the right to a dignified existence, self-determination, and communication with and access to persons and services inside and outside the facility .\n**(3)**\nIn March of 2020, the Centers for Medicare & Medicaid Services instructed nursing facilities to restrict visitation for all visitors and non-essential healthcare personnel and cancel communal dining and group activities. Long-term care ombudsman program representatives and State surveyors were among those whose access to long-term care facilities was prohibited or extremely restricted despite reopening guidance released by the Centers for Medicare & Medicaid Services in May of 2020.\n**(4)**\nMany long-term care residents declined dramatically or died prematurely from failure to thrive in isolation.\n**(5)**\nAccording to the National Consumer Voice for Quality Long-Term Care, in the first year of the COVID\u201319 pandemic, 1 in 5 healthcare workers resigned, retired, or were fired. This exacerbated the longstanding problem of staff shortages that already existed. Lack of staff, combined with the forced absence of families, many of whom provided informal care and support to residents, resulted in a significant decline in residents\u2019 health and well-being. During the pandemic, pressure ulcers in nursing home residents rose by 31 percent, the number of residents experiencing significant weight loss rose by 49 percent, the number of residents reporting feeling down, depressed, or hopeless rose by 40 percent, and the number of residents prescribed antipsychotic medications rose by 77.5 percent.\n**(6)**\nAccording to the Department of Health and Human Services, loneliness and isolation, such as that experienced by long-term care residents during the COVID\u201319 pandemic, represent profound threats to an individual\u2019s health and well-being.\n**(7)**\nEssential Caregivers provide supplemental care for their loved one, regardless of staff shortages, staff turnover, or emergencies. Essential Caregivers support residents and advocate on their behalf.\n#### 3. Right to essential caregivers; access to essential caregivers during periods when visitation is otherwise restricted\n##### (a) Medicare skilled nursing facilities\nSection 1819(c)(3) of the Social Security Act ( 42 U.S.C. 1395i\u20133(c)(3) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively;\n**(2)**\nby striking A skilled nursing facility must\u2014 and inserting the following:\n(A) In general A skilled nursing facility must\u2014 ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Access to essential caregivers during emergency periods when visitation is otherwise restricted (i) Designation of essential caregiver Each skilled nursing facility must recognize the right of each resident of such facility to\u2014 (I) designate and have access to essential caregivers for such resident at all times, including during any period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law; and (II) amend such designation at any time. (ii) Presumption of designation For purposes of clause (i), in the case of a resident who is unable, by reason of cognitive or mental disability, to make an election described in such clause, the resident representative (as defined in section 483.5 of title 42, Code of Federal Regulations) of such resident may make such designation for such resident. (iii) Access to essential caregivers during emergency periods when visitation is otherwise restricted During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a skilled nursing facility must\u2014 (I) not deny in-person access to a resident by an essential caregiver of the resident except as provided in this subparagraph; (II) allow at least 1 essential caregiver to have access to and provide assistance to such resident at such facility every day and at any time; (III) enforce the agreement described in clause (vii)(II) with respect to an essential caregiver; and (IV) provide reasonable accommodations to protect the rights of a roommate co-living with a resident who has an essential caregiver. (iv) Restrictions on access (I) In general During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a skilled nursing facility\u2014 (aa) may, subject to item (bb), deny access to a resident by an essential caregiver of the resident for\u2014 (AA) an initial period of not longer than 7 days; and (BB) one additional period of not longer than 7 days (in addition to the initial period described in subitem (AA)) if the department of health or other applicable agency of the State in which the facility is located approves the denial of access for such additional period; and (bb) must allow access to a resident who is in end-of-life care or a resident in decline or distress, as defined by the Secretary. (II) Rule of application For purposes of subclause (I), a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law shall begin on the date that such order or other operation of law takes effect and shall end on the date that such order or other operation of law expires or is otherwise terminated. During any such period, the maximum number of days for which a skilled nursing facility may deny access to a resident by an essential caregiver of the resident is 7 total days (or, subject to the approval of the department of health or other applicable agency of the State in which the facility is located, 14 total days). (v) Compliance and notification (I) Authority No essential caregiver who upholds the agreement described in clause (vii)(II) shall be denied access to the skilled nursing facility of the resident involved. (II) Notification If an essential caregiver fails to comply with an agreement with a skilled nursing facility described in clause (vii)(II), the facility must first provide a warning to the essential caregiver and resident in writing citing specific issues of non-compliance and providing clear guidance for corrective measures. (III) Enforcement If an essential caregiver or resident, after receiving a notification of noncompliance described in subclause (II), fails to take corrective action, the essential caregiver may subsequently be denied access to the resident. In such cases, the facility shall provide to such caregiver and such resident (or health care proxy of such resident), not later than 24 hours after such denial of access occurs, a written explanation as to why such caregiver was denied access to such resident. Such explanation must include the resident\u2019s and caregiver's options for appeal under the processes established under clause (vi). (vi) Options for residents and caregivers to appeal denials of access (I) In general Not later than 2 years after the date of enactment of this subparagraph, the Secretary shall issue a final rule establishing a process for residents and caregivers to appeal denials of access to the State survey agency. (II) Appeals process The State survey agency shall\u2014 (aa) receive appeals from residents and essential caregivers challenging a decision by a skilled nursing facility to deny access under clause (v); and (bb) begin investigating such appeals not later than 2 business days after receiving such appeals. (III) Burden of proof During an appeal received under the appeals process established under subclause (I), if a skilled nursing facility defends a decision to deny access to an essential caregiver under clause (v) on the basis that the essential caregiver violated the agreement described in clause (vii)(II), the skilled nursing facility shall have the burden of proof in demonstrating that the essential caregiver violated such agreement. (IV) Resolution of appeals (aa) Determination With respect to an appeal received under the appeals process established under subclause (I), the State survey agency shall make a determination as to whether a skilled nursing facility violated a requirement or prohibition of this subparagraph within 48 hours of commencing its investigation. (bb) Violations If the agency determines that a facility has violated such a requirement or prohibition, the agency shall\u2014 (AA) require the facility to allow immediate access to the essential caregiver in question; (BB) require the facility to establish a corrective action plan to prevent the recurrence of such violation within a 7-day period of receiving notice from the agency; and (CC) impose a civil money penalty in an amount to be determined by the agency (not to exceed $5,000) if such facility fails to implement the corrective action plan with the 7-day period specified in subitem (BB). (vii) Definition of essential caregiver For purposes of this subparagraph, the term essential caregiver means, with respect to a resident of a skilled nursing facility, an individual who\u2014 (I) is designated by or on behalf of the resident pursuant to clause (i) or clause (ii); and (II) agrees to follow all safety protocols established by such facility, which shall be clearly specified in writing and may be no more restrictive than the safety protocols (including safety standards and entry requirements) applicable to staff of such facility. .\n##### (b) Medicaid nursing facilities\nSection 1919(c)(3) of the Social Security Act ( 42 U.S.C. 1396r(c)(3) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively;\n**(2)**\nby striking A nursing facility must\u2014 and inserting the following:\n(A) In general A nursing facility must\u2014 ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Access to essential caregivers during emergency periods when visitation is otherwise restricted (i) Designation of essential caregiver Each nursing facility must recognize the right of each resident of such facility to\u2014 (I) designate and have access to essential caregivers for such resident at all times, including during any period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law; and (II) amend such designation at any time. (ii) Presumption of designation For purposes of clause (i), in the case of a resident who is unable, by reason of cognitive or mental disability, to make an election described in such clause, the resident representative (as defined in section 483.5 of title 42, Code of Federal Regulations) of such resident may be permitted to make such designation for such resident. (iii) Access to essential caregivers during emergency periods when visitation is otherwise restricted During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a nursing facility must\u2014 (I) not deny in-person access to a resident by an essential caregiver of the resident except as provided in this subparagraph; (II) allow at least 1 essential caregiver to have access to and provide assistance to such resident at such facility every day and at any time; (III) enforce the agreement described in clause (vii)(II) with respect to an essential caregiver; and (IV) provide reasonable accommodations to protect the rights of a roommate co-living with a resident who has an essential caregiver. (iv) Restrictions on access (I) In general During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a nursing facility\u2014 (aa) may, subject to item (bb), deny access to a resident by an essential caregiver of the resident for\u2014 (AA) an initial period of not longer than 7 days; and (BB) one additional period of not longer than 7 days (in addition to the initial period described in subitem (AA)) if the department of health or other applicable agency of the State in which the facility is located approves the denial of access for such additional period; and (bb) must allow access to a resident who is in end-of-life care or a resident in decline or distress, as defined by the Secretary. (II) Rule of application For purposes of subclause (I), a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law shall begin on the date that such order or other operation of law takes effect and shall end on the date that such order or other operation of law expires or is otherwise terminated. During any such period, the maximum number of days for which a nursing facility may deny access to a resident by an essential caregiver of the resident is 7 total days (or, subject to the approval of the department of health or other applicable agency of the State in which the facility is located, 14 total days). (v) Compliance and notification (I) Authority No essential caregiver who upholds the agreement described in clause (vii)(II) shall be denied access to the nursing facility of the resident involved. (II) Notification If an essential caregiver fails to comply with an agreement with a nursing facility described in clause (vii)(II), the facility must first provide a warning to the essential caregiver and resident in writing citing specific issues of non-compliance and providing clear guidance for corrective measures. (III) Enforcement If an essential caregiver or resident, after receiving a notification of noncompliance described in subclause (II), fails to take corrective action, the essential caregiver may subsequently be denied access to the resident. In such cases, the facility shall provide to such caregiver and such resident (or health care proxy of such resident), not later than 24 hours after such denial of access occurs, a written explanation as to why such caregiver was denied access to such resident. Such explanation must include the resident\u2019s and caregiver's options for appeal under the processes established under clause (vi). (vi) Options for residents and caregivers to appeal denials of access (I) In general Not later than 2 years after the date of enactment of this subparagraph, the Secretary shall issue a final rule establishing a process for residents and caregivers to appeal denials of access to the State survey agency. (II) Appeals process The State survey agency shall\u2014 (aa) receive appeals from residents and essential caregivers challenging a decision by a nursing facility to deny access under clause (v); and (bb) begin investigating such appeals not later than 2 business days after receiving such appeals. (III) Burden of proof During an appeal received under the appeals process established under subclause (I), if a nursing facility defends a decision to deny access to an essential caregiver under clause (v) on the basis that the essential caregiver violated the agreement described in clause (vii)(II), the nursing facility shall have the burden of proof in demonstrating that the essential caregiver violated such agreement. (IV) Resolution of appeals (aa) Determination With respect to an appeal received under the appeals process established under subclause (I), the State survey agency shall make a determination as to whether a nursing facility violated a requirement or prohibition of this subparagraph within 48 hours of commencing its investigation. (bb) Violations If the agency determines that a facility has violated such a requirement or prohibition, the agency shall\u2014 (AA) require the facility to allow immediate access to the essential caregiver in question; (BB) require the facility to establish a corrective action plan to prevent the recurrence of such violation within a 7-day period of receiving notice from the agency; and (CC) impose a civil money penalty in an amount to be determined by the agency (not to exceed $5,000) if such facility fails to implement the corrective action plan with the 7-day period specified in subitem (BB). (vii) Definition of essential caregiver For purposes of this subparagraph, the term essential caregiver means, with respect to a resident of a nursing facility, an individual who\u2014 (I) is designated by or on behalf of the resident pursuant to clause (i) or clause (ii); and (II) agrees to follow all safety protocols established by such facility, which shall be clearly specified in writing and may be no more restrictive than the safety protocols (including safety standards and entry requirements) applicable to staff of such facility. .\n##### (c) Intermediate care facilities for the intellectually disabled\nSection 1905(d) of the Social Security Act ( 42 U.S.C. 1396d(d) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(4) the institution complies with the requirements relating to the designation of, and access to residents by, essential caregivers described in section 1919(c)(3)(B) in the same manner as if such institution were a nursing facility. .\n##### (d) Inpatient rehabilitation facilities\nSection 1866(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (X), by striking and at the end;\n**(2)**\nin subparagraph (Y), by striking the period at the end and inserting , and ; and\n**(3)**\nby inserting after subparagraph (Y) the following new subparagraph:\n(Z) in the case of an inpatient rehabilitation facility that is located on the same campus (as defined by the Secretary) as a skilled nursing facility, nursing facility (as defined in section 1919(a)), or intermediate care facility for the intellectually disabled (as described in section 1905(d)), to comply with the requirements relating to the designation of, and access to residents by, essential caregivers described in section 1819(c)(3)(B) in the same manner as if such institution were a skilled nursing facility. .\n##### (e) Regulations\nThe Secretary of Health and Human Services shall, after consultation with stakeholders (including residents, family members, long-term care ombudsmen, other advocates of nursing home residents, and nursing home providers), promulgate regulations to carry out this Act and the amendments made by this Act.\n##### (f) Rules of construction\n**(1) No new authority for State and local officials to restrict visitation at nursing facilities**\nNothing in this section or the amendments made by this section shall be construed as creating any new authority for State or local officials to restrict visitation at nursing facilities.\n**(2) No new authority for nursing facilities to unilaterally restrict visitation**\nNothing in this section or the amendments made by this section shall be construed as creating any new authority for a skilled nursing facility or nursing facility (as such terms are defined in sections 1819 and 1919 of the Social Security Act, respectively ( 42 U.S.C. 1395i\u20133 , 1396r)) to restrict visitation.\n##### (g) Effective date\nThe amendments made by this Act shall take effect on the date that is 2 years after the date of enactment of this Act, and shall apply with respect to periods beginning on or after such date in which regular visitation at nursing facilities is restricted by order of a Federal, State, or local authority or by other operation of law.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-16",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6766",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Essential Caregivers Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-12T16:41:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s3492",
          "measure-number": "3492",
          "measure-type": "s",
          "orig-publish-date": "2025-12-16",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3492v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-12-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>"
        },
        "title": "Essential Caregivers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3492.xml",
    "summary": {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s3492"
    },
    "title": "Essential Caregivers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s3492"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3492is.xml"
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
      "title": "Essential Caregivers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Essential Caregivers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:24:10Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act to require skilled nursing facilities, nursing facilities, intermediate care facilities for the intellectually disabled, and inpatient rehabilitation facilities to permit essential caregivers access during any period in which regular visitation is restricted.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:18:26Z"
    }
  ]
}
```
