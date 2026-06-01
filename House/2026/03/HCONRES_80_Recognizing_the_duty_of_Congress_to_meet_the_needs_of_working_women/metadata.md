# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/80?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/80
- Title: Recognizing the duty of Congress to meet the needs of working women.
- Congress: 119
- Bill type: HCONRES
- Bill number: 80
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-28T08:06:16Z
- Update date including text: 2026-04-28T08:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-25 - IntroReferral: Submitted in House
- 2026-03-25 - IntroReferral: Submitted in House
- Latest action: 2026-03-25: Submitted in House

## Actions

- 2026-03-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-25 - IntroReferral: Submitted in House
- 2026-03-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/80",
    "number": "80",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Recognizing the duty of Congress to meet the needs of working women.",
    "type": "HCONRES",
    "updateDate": "2026-04-28T08:06:16Z",
    "updateDateIncludingText": "2026-04-28T08:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-25T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "OR"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NJ"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "ME"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "OR"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "TN"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres80ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 80\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mrs. McIver (for herself, Ms. DeLauro , Ms. Leger Fernandez , Ms. Norton , Mr. Goldman of New York , Ms. Wilson of Florida , Mr. Tonko , Ms. Schakowsky , Ms. McBride , Mr. Krishnamoorthi , Ms. Simon , Mrs. Dingell , and Mrs. Ramirez ) submitted the following concurrent resolution; which was referred to the Committee on Education and Workforce\nCONCURRENT RESOLUTION\nRecognizing the duty of Congress to meet the needs of working women.\nThat Congress\u2014\n**(1)**\nrecognizes an affirmative duty to ensure women have equal opportunity within the workforce, as a prerequisite for economic security, democratic participation, shared prosperity, and full participation in public life;\n**(2)**\nrecognizes that the workforce of the Nation is stronger, more innovative, and more competitive when women are able to contribute and lead across all industries;\n**(3)**\naffirms its commitment to economic prosperity for all, including\u2014\n**(A)**\nequal pay for equal work;\n**(B)**\npay transparency;\n**(C)**\nworkplaces free from discrimination;\n**(D)**\nworkplace safety standards and regulations designed to protect the health of the Nation\u2019s workers;\n**(E)**\ncomprehensive and accessible health care, including reproductive health care;\n**(F)**\naffordable, high-quality childcare and early education;\n**(G)**\npaid family and medical leave;\n**(H)**\npaid sick days;\n**(I)**\npredictable scheduling and fair labor standards; and\n**(J)**\naccess to affordable housing, education, and workforce development opportunities;\n**(4)**\naffirms its commitment to ensuring that all women, regardless of race, immigration status, language, or occupation, are able to work with dignity, free from violence, harassment, discrimination, retaliation, and abuse;\n**(5)**\nrecognizes the value of all work, especially domestic and part-time work, and recognizes its obligation to ensure that such work is dignified with fair pay, benefits, protections, and working conditions;\n**(6)**\ncondemns actions and policies that weaken civil rights enforcement, undermine workplace protections, reduce access to health care and essential services, or otherwise threaten the economic security of working women;\n**(7)**\ncommits itself to restoring and strengthening Federal agencies that combat discrimination in the workplace, including the Equal Employment Opportunity Commission and the Office of Federal Contract Compliance Programs;\n**(8)**\nreaffirms its commitment to ensuring all people can live a life with dignity by raising wages, including by raising the Federal minimum wage, and eliminating tipped and subminimum wages;\n**(9)**\nreaffirms its commitment to expanding access to high-paying jobs across gender lines by strengthening programs that dismantle occupational segregation;\n**(10)**\nrecognizes the right of every worker to join a union, free from interference and intimidation, and bargain collectively for fair wages and working conditions;\n**(11)**\ncalls upon Federal, State, and local governments, employers, labor organizations, and community institutions to work collaboratively to ensure that all working women have the opportunity to thrive and be free from harassment and discrimination; and\n**(12)**\ndeclares that addressing the immediate needs of working women is essential to the prosperity of the United States.",
      "versionDate": "2026-03-25",
      "versionType": "IH"
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
        "actionDate": "2026-03-25",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1619)"
      },
      "number": "31",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A concurrent resolution recognizing the duty of Congress to meet the needs of working women.",
      "type": "SCONRES"
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
        "updateDate": "2026-04-02T17:51:42Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres80ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the duty of Congress to meet the needs of working women.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T08:18:31Z"
    },
    {
      "title": "Recognizing the duty of Congress to meet the needs of working women.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T08:06:38Z"
    }
  ]
}
```
