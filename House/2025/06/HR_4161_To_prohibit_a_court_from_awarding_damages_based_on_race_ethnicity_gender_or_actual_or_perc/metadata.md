# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4161
- Title: Fair Calculations in Civil Damages Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4161
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-12-05T21:50:06Z
- Update date including text: 2025-12-05T21:50:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4161",
    "number": "4161",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Fair Calculations in Civil Damages Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:50:06Z",
    "updateDateIncludingText": "2025-12-05T21:50:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:02:15Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "DC"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4161ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4161\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Casten (for himself and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit a court from awarding damages based on race, ethnicity, gender, or actual or perceived sexual orientation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Calculations in Civil Damages Act of 2025 .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term future earnings table includes any table or compilation of economic data used to determine, taking into account the median earnings in a geographic region\u2014\n**(A)**\nhow many years an individual would have worked in the future; or\n**(B)**\nthe average wage an individual would have earned in the future; and\n**(2)**\nthe term protected class means a group of individuals sharing a common characteristic or identity who are legally protected against discrimination.\n#### 3. Calculations of damages\n##### (a) In general\nNotwithstanding any other provision of law, no court of the United States may award damages to a plaintiff in a civil action using a calculation for the projected future earning potential of that plaintiff that takes into account the actual or perceived race, ethnicity, or sex (including gender, gender identity, sexual orientation, and sex characteristics including intersex traits).\n##### (b) Rule of construction\nNothing in this section shall be construed to deny a court from ordering damages based on the fact that the plaintiff is a member of a protected class or for the purposes of Federal civil rights laws.\n#### 4. Inclusive future earnings tables\nNot later than 180 days after the date of enactment of this Act\u2014\n**(1)**\nthe Secretary of Labor shall develop guidance for forensic economists to develop inclusive future earnings tables that do not rely on race, ethnicity, gender, or actual or perceived sexual orientation; and\n**(2)**\nthe Secretary of Labor and the Attorney General shall develop guidance for States on how to make calculations of future earnings in State tort proceedings free of bias on the basis of actual or perceived race, ethnicity, and sex (including gender, gender identity, sexual orientation, and sex characteristics including intersex traits).\n#### 5. Study and report\n##### (a) Judicial Conference of the United States\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Judicial Conference of the United States shall conduct a study on\u2014\n**(A)**\ndamages awarded under Federal law for personal injury; and\n**(B)**\nthe aggregate data described in paragraph (1)\u2014\n**(i)**\nby case type, including employment discrimination and tort damages; or\n**(ii)**\nby protected classes, including actual or perceived race, ethnicity, and sex (including gender, gender identity, sexual orientation, and sex characteristics including intersex traits).\n**(2) Report**\nNot later than 18 months after the date of enactment of this Act, the Judicial Conference of the United States shall submit to Congress a report on the study conducted under paragraph (1).\n##### (b) Administrative Office of the United States Courts\nNot later than 1 year after the date of enactment of this Act, the Administrative Office of the United States Courts shall conduct a study and submit to Congress recommendations resulting from the study on how to ensure that calculations of future earning potential of plaintiffs that take into account age and disability without conflicting with Federal equal protection laws.\n#### 6. Training\nThe Federal Judicial Center shall conduct training for Federal judges on how to implement this Act, including instructions on how to use tables on future earnings in evidence that comply with this Act.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-06-26",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2190",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fair Calculations in Civil Damages Act of 2025",
      "type": "S"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-07-15T11:10:29Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4161ih.xml"
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
      "title": "Fair Calculations in Civil Damages Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Calculations in Civil Damages Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a court from awarding damages based on race, ethnicity, gender, or actual or perceived sexual orientation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:27Z"
    }
  ]
}
```
