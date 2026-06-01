# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3336?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3336
- Title: Reliable Artificial Intelligence Research Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3336
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-01-07T17:33:54Z
- Update date including text: 2026-01-07T17:33:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3336",
    "number": "3336",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Reliable Artificial Intelligence Research Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T17:33:54Z",
    "updateDateIncludingText": "2026-01-07T17:33:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T21:25:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3336is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3336\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Ms. Hassan (for herself and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Secretary of Homeland Security to carry out prize competitions to advance the science of interpretability and to develop adversarial robustness with respect to artificial intelligence products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reliable Artificial Intelligence Research Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Adversarial robustness**\nThe term adversarial robustness means the degree to which an artificial intelligence model is able to resist attacks that would induce it to produce incorrect, restricted, or harmful outputs, while maintaining integrity, reliability, and privacy.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Interpretability**\nThe term interpretability means the degree to which humans are able to accurately understand how an artificial intelligence model makes decisions and considers inputs and how the outputs or behaviors of the model respond to a change in the inputs.\n**(4) Red-teaming**\nThe term red-teaming means a structured, interactive, and adversarial process to test an artificial intelligence system by simulating real-world actions to find vulnerabilities or flaws in the system.\n**(5) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Prize competition for artificial intelligence interpretability research\n##### (a) Prize competition required\nNot later than 270 days after the date of enactment of this Act, the Secretary of Homeland Security shall commence carrying out at least 1 prize competition under section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719 ) to advance the science of interpretability in a manner relevant to commercially available or widely used artificial intelligence products.\n##### (b) Consultation\nIn carrying out the prize competition required by subsection (a), the Secretary shall consult with\u2014\n**(1)**\nthe Secretary of Commerce;\n**(2)**\nthe Director of the National Institute of Standards and Technology;\n**(3)**\nthe National Cyber Director;\n**(4)**\nthe Director of the National Science Foundation; and\n**(5)**\nany industry expert from the artificial intelligence sector in the United States that the Secretary considers relevant.\n##### (c) Structure and evaluation criteria\n**(1) In general**\nThe Secretary shall develop the structure and evaluation criteria for a prize competition carried out under subsection (a) in accordance with the primary purpose described in that subsection.\n**(2) Competition structure**\nThe Secretary may\u2014\n**(A)**\nstructure a competition under subsection (a) into 1 or more phases, including submission of interpretability frameworks, submission of interpretable artificial intelligence models, and unique basic research; and\n**(B)**\nopen these phases to the same, or to distinct, contestant pools.\n**(3) Evaluation considerations**\nIn developing the evaluation criteria for the frameworks, models, or methods submitted for a prize competition under subsection (a), the Secretary shall consider\u2014\n**(A)**\nthe degree to which a submission advances broadly applicable principles of artificial intelligence interpretability;\n**(B)**\nthe practical value of a submission in making artificial intelligence more understandable and reliable in high-risk, high-value use cases; and\n**(C)**\nthe likelihood that the unique research submitted will create standards for artificial intelligence interpretability in the government or industry.\n##### (d) Program administration\nThe Secretary may enter into contracts, cooperative agreements, or other agreements with for-profit or nonprofit entities or State, territorial, local, or Tribal agencies to design and administer any prize competition carried out under subsection (a).\n#### 4. Prize competition for artificial intelligence adversarial robustness research\n##### (a) Prize competition required\nNot later than 270 days after the date of enactment of this Act, the Secretary shall commence carrying out at least 1 prize competition under section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719 ) to develop capable artificial intelligence models that are designed to exhibit adversarial robustness in circumstances necessary for at least 1 high-impact, high-risk application in government or industry.\n##### (b) Consultation\nIn carrying out a prize competition required by subsection (a), the Secretary shall consult with\u2014\n**(1)**\nthe Secretary of Commerce;\n**(2)**\nthe Director of the Institute of Standards and Technology;\n**(3)**\nthe National Cyber Director;\n**(4)**\nthe Director of the National Science Foundation;\n**(5)**\nany industry expert from the artificial intelligence sector in the United States that the Secretary considers relevant; and\n**(6)**\nthe head of any Federal agency who has authority or expertise in a high-impact, high-risk application of artificial intelligence that could be an appropriate subject for a prize competition under subsection (a).\n##### (c) Structure and evaluation criteria\n**(1) In general**\nThe Secretary shall develop the structure and evaluation criteria for a prize competition carried out under subsection (a) in accordance with the primary purpose described in that subsection.\n**(2) Competition structure**\nThe Secretary may\u2014\n**(A)**\nstructure a competition under subsection (a) into 1 or more phases, including submission of adversarial robustness frameworks, submission of artificial intelligence models, and red-teaming; and\n**(B)**\nopen these phases to the same, or to distinct, contestant pools.\n**(3) Evaluation considerations**\nIn developing the evaluation criteria for the frameworks, models, or methods submitted for a prize competition under subsection (a), the Secretary shall consider\u2014\n**(A)**\nthe degree to which a submission advances broadly applicable principles of artificial intelligence robustness; and\n**(B)**\nthe practical value of the submission in reducing the risk of adversarial attacks in high-risk, high-value use cases of artificial intelligence.\n##### (d) Program administration\nThe Secretary may enter into contracts, cooperative agreements, or other agreements with for-profit or nonprofit entities or State, territorial, local, or Tribal agencies to design and administer any prize competition carried out under subsection (a).\n#### 5. Tracking and reporting\n##### (a) In general\nNot later than 180 days after the date on which the first prize competition concludes, the Secretary shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\nan evaluation of how the results of the competitions inform the fields of interpretability and adversarial robustness;\n**(2)**\nan assessment of any gaps in these fields identified by the Secretary over the course of the competitions; and\n**(3)**\nany suggested action that Congress should take to advance the fields of interpretability, adversarial robustness, and any related research.\n##### (b) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(2)**\nthe Committee on Homeland Security of the House of Representatives.\n#### 6. Appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $10,000,000 for the period of fiscal years 2026 through 2030.",
      "versionDate": "2025-12-03",
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
        "updateDate": "2026-01-07T17:33:54Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3336is.xml"
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
      "title": "Reliable Artificial Intelligence Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reliable Artificial Intelligence Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security to carry out prize competitions to advance the science of interpretability and to develop adversarial robustness with respect to artificial intelligence products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:21Z"
    }
  ]
}
```
