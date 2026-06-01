# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3524
- Title: Protect Patriot Spouses Act
- Congress: 119
- Bill type: HR
- Bill number: 3524
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2025-12-05T21:50:19Z
- Update date including text: 2025-12-05T21:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3524",
    "number": "3524",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001200",
        "district": "9",
        "firstName": "Darren",
        "fullName": "Rep. Soto, Darren [D-FL-9]",
        "lastName": "Soto",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Protect Patriot Spouses Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:50:19Z",
    "updateDateIncludingText": "2025-12-05T21:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T14:02:10Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3524ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3524\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2025 Mr. Soto (for himself, Mr. Carbajal , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo render certain military spouses eligible for adjustment of status, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Patriot Spouses Act .\n#### 2. Adjustment of status for certain military spouses\nSection 245 of the Immigration and Nationality Act ( 8 U.S.C. 1255 ) is amended by adding at the end the following:\n(o) (1) In applying this section to an alien described in paragraph (2)\u2014 (A) such alien shall be deemed, for purposes of subsection (a), to have been inspected and admitted into the United States; and (B) in determining the alien\u2019s admissibility as an immigrant\u2014 (i) paragraphs (6)(A), (7)(A), and (9)(B) of section 212(a) shall not apply; and (ii) the Secretary of Homeland Security, in the discretion of the Secretary, may waive the application of paragraphs (6)(C), (9)(A), and (9)(C) of section 212(a) if the alien establishes to the satisfaction of the Secretary that the alien does not pose a threat to the public and has not committed any criminal offenses in violation of Federal or State law unrelated to the alien\u2019s status. (2) An alien is described in this paragraph if the alien\u2014 (A) is or was the spouse of a United States citizen who\u2014 (i) is or was serving on active duty in the United States Armed Forces or in a reserve component of the United States Armed Forces; and (ii) if discharged or released from service in the Armed Forces, was discharged or released under honorable conditions; and (B) is the beneficiary of a petition for classification under section 204(a)(1)(A) as an immediate relative (as defined in section 201(b)) by reason of the marriage to such citizen. .\n#### 3. Treatment of certain grounds for inadmissibility for certain military spouses\nSection 212 of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended by inserting after subsection (b) the following:\n(c) (1) In determining the admissibility as an immigrant of an alien described in paragraph (2)\u2014 (A) subsection (a)(9)(B) shall not apply; and (B) the Secretary of Homeland Security, in the discretion of the Secretary, may waive the application of paragraphs (6)(C), (9)(A), and (9)(C) of subsection (a) if the alien establishes to the satisfaction of the Secretary that the alien does not pose a threat to the public and has not committed any criminal offenses in violation of Federal or State law unrelated to the alien\u2019s status. (2) An alien is described in this paragraph if the alien\u2014 (A) is or was the spouse of a United States citizen who\u2014 (i) is or was serving on active duty in the United States Armed Forces or in a reserve component of the United States Armed Forces; and (ii) if discharged or released from service in the Armed Forces, was discharged or released under honorable conditions; and (B) is the beneficiary of a petition for classification under section 204(a)(1)(A) as an immediate relative (as defined in section 201(b)) by reason of the marriage to such citizen. .\n#### 4. Eligibility of removed or voluntarily departed aliens\n##### (a) In general\nThe Secretary of Homeland Security and the Secretary of State shall take such steps as may be necessary to ensure that eligible aliens who were removed or permitted to depart voluntarily from the United States before the date of the enactment of this Act may apply from abroad for an immigrant visa pursuant to the amendment made by section 3.\n##### (b) Nonimmigrant admission pending adjudication\nThe Secretary of Homeland Security and the Secretary of State shall establish a program under which an eligible alien with a pending application made under subsection (a) may be authorized to enter the United States as a nonimmigrant to reunite with their United States citizen spouse during the period in which such application, and an associated application for adjustment of status, remain pending. In determining whether an alien is eligible to be admitted to the United States as a nonimmigrant under this subsection, the Secretary of Homeland Security and the Secretary of State shall require the alien to establish to the satisfaction of each Secretary that the alien does not pose a threat to the public or to national security. In determining the admissibility as a nonimmigrant of an alien described in this subsection, the Secretary of Homeland Security, in the discretion of the Secretary, may waive the application of paragraphs (6)(C) and (9) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ).",
      "versionDate": "2025-05-20",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3529",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Patriot Parents Act",
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
        "name": "Immigration",
        "updateDate": "2025-05-29T15:31:50Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3524ih.xml"
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
      "title": "Protect Patriot Spouses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Patriot Spouses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To render certain military spouses eligible for adjustment of status, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:41Z"
    }
  ]
}
```
