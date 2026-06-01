# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/272
- Title: Protect Infant Formula from Contamination Act
- Congress: 119
- Bill type: S
- Bill number: 272
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-05-05T08:05:57Z
- Update date including text: 2026-05-05T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-01-15 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 306.
- 2026-04-28 - Floor: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2074-2075; text: CR S2074)
- 2026-04-28 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:39 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-01-15 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-01-28 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 306.
- 2026-04-28 - Floor: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2074-2075; text: CR S2074)
- 2026-04-28 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:39 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/272",
    "number": "272",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Protect Infant Formula from Contamination Act",
    "type": "S",
    "updateDate": "2026-05-05T08:05:57Z",
    "updateDateIncludingText": "2026-05-05T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-04",
      "actionTime": "10:33:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-04",
      "actionTime": "10:32:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2074-2075; text: CR S2074)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 306.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute and an amendment to the title. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
            "date": "2026-01-28T19:52:51Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-15T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-28T19:28:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-28T19:28:36Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "ND"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ME"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NH"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NH"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "WI"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "WA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s272is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 272\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Peters (for himself and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve the safety of infant formula through testing of infant formula for microorganisms and toxic elements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Infant Formula from Contamination Act .\n#### 2. Notifications for testing of infant formula\nSection 412(e) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a(e) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter following subparagraph (B)\u2014\n**(A)**\nby striking promptly ;\n**(B)**\nby inserting , within 1 business day of acquiring such knowledge after such knowledge ; and\n**(C)**\nby striking the infant formula and inserting an infant formula ;\n**(2)**\nby redesignating paragraph (2) as paragraph (5); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) If the result of any testing of a sample from any production aggregate of finished infant formula product is confirmed as a positive analytical result for any microorganism for which finished product testing is required under section 106.55(e) of title 21, Code of Federal Regulations (or any successor regulation), the manufacturer shall\u2014 (A) within 1 business day of acquiring a confirmed positive analytical result, notify the Secretary of such result, regardless of whether such product has left an establishment subject to the control of the manufacturer; (B) promptly consult with the Secretary for proper isolation of the affected product, and, as the Secretary may require, cease distribution and properly dispose of the affected product; and (C) promptly provide to the Secretary results and isolates from a positive sample of such product or the whole genetic sequence from any confirmed positive analytical result. (3) Not later than 1 business day after receipt by the Secretary of a notification under paragraph (2)(A), the Secretary shall respond to the manufacturer of the infant formula to begin discussions regarding investigation and corrective action, and, as appropriate, share the findings of the Secretary with the manufacturer. (4) Not later than 90 days after receipt of a notification under paragraph (1) or (2), the Secretary shall confirm, including through the collection of documentation, that the manufacturer submitting the notification performed, or is performing, an appropriate investigation and corrective action, if applicable. The Secretary shall consider, as part of the review of the root cause investigation, the analytical method used to conduct laboratory testing and, as appropriate, the potential for cross contamination of the sample by handling and testing. The manufacturer shall make such documentation available to the Secretary electronically and for inspection under section 704. .\n#### 3. Reporting to improve the safety and supply of infant formula\nSection 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) is amended by adding at the end the following:\n(n) Reporting To improve the safety and supply of infant formula (1) Progress report Not later than 180 days after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall issue a progress report on implementation of the recommendations to improve the safety and supply of infant formula contained in the report titled, Long-Term National Strategy to Increase the Resiliency of the U.S. Infant Formula Market , issued by the Food and Drug Administration in January 2025. Such progress report shall include additional authorities or resources that the Secretary may require for purposes of improving the safety and supply of infant formula. (2) Quarterly reports on supply chain Not later than 270 days after the date of enactment of the Protect Infant Formula from Contamination Act , and not less frequently than quarterly for the 5-year period thereafter, the Secretary shall submit a report on the most current, critical supply chain data for infant formula, including in-stock rates, to\u2014 (A) the Committee on Health, Education, Labor, and Pensions; the Committee on Agriculture, Nutrition, and Forestry; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the Senate; and (B) the Committee on Energy and Commerce; the Committee on Agriculture; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the House of Representatives. (3) Consultation The Secretary shall engage with the Department of Agriculture and other relevant agencies of the Federal Government regarding ongoing efforts to address immediate formula needs and build long-term resiliency into the infant formula market. (4) Reports on adequacy of supply Not later than 1 year, 3 years, and 5 years after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall\u2014 (A) engage with public stakeholders, infant formula manufacturers, and other stakeholders, as determined by the Secretary, to determine evidence-based practices that can be implemented to maximize infant formula supply and infant safety, which may include the value of high frequency testing for purposes of identifying contamination events and bracketing potentially contaminated product, the impact of corrective action on contamination events, and evidence-based recommendations for enhancing infant formula supply and safety; and (B) submit a report to the committees described in subparagraphs (A) and (B) of paragraph (2) that identifies the modifications to manufacturer practices and actions described in subparagraph (A), if any, that could be implemented to improve infant formula supply and safety. .",
      "versionDate": "2025-02-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s272rs.xml",
      "text": "II\nCalendar No. 306\n119th CONGRESS\n2d Session\nS. 272\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Peters (for himself, Mr. Hoeven , Ms. Collins , Ms. Smith , Mrs. Shaheen , Ms. Hassan , Mr. Kaine , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nJanuary 28, 2026 Reported by Mr. Cassidy , with an amendment and an amendment to the title Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo improve the safety of infant formula through testing of infant formula for microorganisms and toxic elements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Infant Formula from Contamination Act .\n#### 2. Notifications for testing of infant formula\nSection 412(e) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a(e) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter following subparagraph (B)\u2014\n**(A)**\nby striking promptly ;\n**(B)**\nby inserting , within 1 business day of acquiring such knowledge after such knowledge ; and\n**(C)**\nby striking the infant formula and inserting an infant formula ;\n**(2)**\nby redesignating paragraph (2) as paragraph (5); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) If the result of any testing of a sample from any production aggregate of finished infant formula product is confirmed as a positive analytical result for any microorganism for which finished product testing is required under section 106.55(e) of title 21, Code of Federal Regulations (or any successor regulation), the manufacturer shall\u2014 (A) within 1 business day of acquiring a confirmed positive analytical result, notify the Secretary of such result, regardless of whether such product has left an establishment subject to the control of the manufacturer; (B) promptly consult with the Secretary for proper isolation of the affected product, and, as the Secretary may require, cease distribution and properly dispose of the affected product; and (C) promptly provide to the Secretary results and isolates from a positive sample of such product or the whole genetic sequence from any confirmed positive analytical result. (3) Not later than 1 business day after receipt by the Secretary of a notification under paragraph (2)(A), the Secretary shall respond to the manufacturer of the infant formula to begin discussions regarding investigation and corrective action, and, as appropriate, share the findings of the Secretary with the manufacturer. (4) Not later than 90 days after receipt of a notification under paragraph (1) or (2), the Secretary shall confirm, including through the collection of documentation, that the manufacturer submitting the notification performed, or is performing, an appropriate investigation and corrective action, if applicable. The Secretary shall consider, as part of the review of the root cause investigation, the analytical method used to conduct laboratory testing and, as appropriate, the potential for cross contamination of the sample by handling and testing. The manufacturer shall make such documentation available to the Secretary electronically and for inspection under section 704. .\n#### 3. Reporting to improve the safety and supply of infant formula\nSection 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) is amended by adding at the end the following:\n(n) Reporting To improve the safety and supply of infant formula (1) Progress report Not later than 180 days after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall issue a progress report on implementation of the recommendations to improve the safety and supply of infant formula contained in the report titled, Long-Term National Strategy to Increase the Resiliency of the U.S. Infant Formula Market , issued by the Food and Drug Administration in January 2025. Such progress report shall include additional authorities or resources that the Secretary may require for purposes of improving the safety and supply of infant formula. (2) Quarterly reports on supply chain Not later than 270 days after the date of enactment of the Protect Infant Formula from Contamination Act , and not less frequently than quarterly for the 5-year period thereafter, the Secretary shall submit a report on the most current, critical supply chain data for infant formula, including in-stock rates, to\u2014 (A) the Committee on Health, Education, Labor, and Pensions; the Committee on Agriculture, Nutrition, and Forestry; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the Senate; and (B) the Committee on Energy and Commerce; the Committee on Agriculture; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the House of Representatives. (3) Consultation The Secretary shall engage with the Department of Agriculture and other relevant agencies of the Federal Government regarding ongoing efforts to address immediate formula needs and build long-term resiliency into the infant formula market. (4) Reports on adequacy of supply Not later than 1 year, 3 years, and 5 years after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall\u2014 (A) engage with public stakeholders, infant formula manufacturers, and other stakeholders, as determined by the Secretary, to determine evidence-based practices that can be implemented to maximize infant formula supply and infant safety, which may include the value of high frequency testing for purposes of identifying contamination events and bracketing potentially contaminated product, the impact of corrective action on contamination events, and evidence-based recommendations for enhancing infant formula supply and safety; and (B) submit a report to the committees described in subparagraphs (A) and (B) of paragraph (2) that identifies the modifications to manufacturer practices and actions described in subparagraph (A), if any, that could be implemented to improve infant formula supply and safety. .",
      "versionDate": "2026-01-28",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s272es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 272\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo improve the safety of infant formula through testing of infant formula for microorganisms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Infant Formula from Contamination Act .\n#### 2. Notifications for testing of infant formula\nSection 412(e) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a(e) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter following subparagraph (B)\u2014\n**(A)**\nby striking promptly ;\n**(B)**\nby inserting , within 1 business day of acquiring such knowledge after such knowledge ; and\n**(C)**\nby striking the infant formula and inserting an infant formula ;\n**(2)**\nby redesignating paragraph (2) as paragraph (5); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) If the result of any testing of a sample from any production aggregate of finished infant formula product is confirmed as a positive analytical result for any microorganism for which finished product testing is required under section 106.55(e) of title 21, Code of Federal Regulations (or any successor regulation), the manufacturer shall\u2014 (A) within 1 business day of acquiring a confirmed positive analytical result, notify the Secretary of such result, regardless of whether such product has left an establishment subject to the control of the manufacturer; (B) promptly consult with the Secretary for proper isolation of the affected product, and, as the Secretary may require, cease distribution and properly dispose of the affected product; and (C) promptly provide to the Secretary results and isolates from a positive sample of such product or the whole genome sequence data from any confirmed positive analytical result. (3) Not later than 1 business day after receipt by the Secretary of a notification under paragraph (2)(A), the Secretary shall respond to the manufacturer of the infant formula to begin discussions regarding investigation and corrective action, and, as appropriate, share the findings of the Secretary with the manufacturer. (4) Not later than 90 days after receipt of a notification under paragraph (1) or (2), the Secretary shall confirm, including through the collection of documentation, that the manufacturer submitting the notification performed, or is performing, an appropriate investigation and corrective action, if applicable. The Secretary shall consider, as part of the review of the root cause investigation, the analytical method used to conduct laboratory testing and, as appropriate, the potential for cross contamination of the sample by handling and testing. The manufacturer shall make such documentation available to the Secretary electronically and for inspection under section 704. .\n#### 3. Reporting to improve the safety and supply of infant formula\nSection 412 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350a ) is amended by adding at the end the following:\n(n) Reporting To improve the safety and supply of infant formula (1) Progress report Not later than 180 days after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall issue a progress report on implementation of the recommendations to improve the safety and supply of infant formula contained in the report titled, Long-Term National Strategy to Increase the Resiliency of the U.S. Infant Formula Market , issued by the Food and Drug Administration in January 2025. Such progress report shall include additional authorities or resources that the Secretary may require for purposes of improving the safety and supply of infant formula and any revisions to the recommendations as a result of any infant formula recalls since the publication of the report, as appropriate. (2) Quarterly reports on supply chain Not later than 270 days after the date of enactment of the Protect Infant Formula from Contamination Act , and not less frequently than quarterly for the 5-year period thereafter, the Secretary shall submit a report on the most current critical supply chain data for infant formula, including in-stock rates, to\u2014 (A) the Committee on Health, Education, Labor, and Pensions; the Committee on Agriculture, Nutrition, and Forestry; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the Senate; and (B) the Committee on Energy and Commerce; the Committee on Agriculture; and the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the House of Representatives. (3) Consultation The Secretary shall engage with the Department of Agriculture and other relevant agencies of the Federal Government regarding ongoing efforts to address immediate formula needs and build long-term resiliency into the infant formula market. (4) Reports on adequacy of supply Not later than 1 year, 3 years, and 5 years after the date of enactment of the Protect Infant Formula from Contamination Act , the Secretary shall\u2014 (A) engage with public stakeholders, infant formula manufacturers, and other stakeholders, as determined by the Secretary, to determine evidence-based practices that can be implemented to maximize infant formula supply and infant safety, which may include the value of high frequency testing for purposes of identifying contamination events, including events associated with botulism or other contaminants, and bracketing potentially contaminated product, the impact of corrective action on contamination events, including events associated with botulism or other contaminants, and evidence-based recommendations for enhancing infant formula supply and safety; and (B) submit a report to the committees described in subparagraphs (A) and (B) of paragraph (2) that identifies the modifications to manufacturer practices and actions described in subparagraph (A), if any, that could be implemented to improve infant formula supply and safety. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-04-01T15:18:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:19:06Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-04-01T15:18:57Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2025-04-01T15:18:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-01T15:19:01Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-01T15:18:44Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-04-01T15:18:51Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T17:29:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-06T13:21:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119s272",
          "measure-number": "272",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s272v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Infant Formula from Contamination Act</strong></p><p>This bill imposes certain new requirements on infant formula manufacturers and the Food and Drug Administration (FDA) following the discovery of contaminated, adulterated, or misbranded infant formula.\u00a0</p><p>Specifically, the bill requires infant formula manufacturers to report to the\u00a0FDA\u00a0within one business day of learning that formula that was\u00a0processed by the manufacturer but that is\u00a0no longer within the manufacturer\u2019s control may not provide required nutrients or may be otherwise adulterated or misbranded.\u00a0</p><p>Further, if any testing of finished infant formula reveals the presence of specified microorganisms (e.g., salmonella), the manufacturer must notify the FDA\u00a0within one business day. (Under current law, manufacturers are only required to report contamination to the FDA\u00a0if the affected formula has left the manufacturer\u2019s control.) The manufacturer must also promptly provide the test results to the FDA and consult with the FDA on proper isolation and disposal of the affected product. The FDA must respond to such a notification and begin discussing proper investigative and corrective action with the manufacturer within one business day.\u00a0</p><p>Within 90 days of a report of adulterated, misbranded, or contaminated infant formula, the FDA must determine whether the manufacturer that reported the problem has performed, or is performing, appropriate investigative and corrective action.\u00a0</p><p>Finally, the FDA is required to periodically report on the infant formula supply chain and efforts to improve the safety and supply of infant formula, and must consult with other federal agencies and infant formula stakeholders on these issues. \u00a0</p>"
        },
        "title": "Protect Infant Formula from Contamination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s272.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Infant Formula from Contamination Act</strong></p><p>This bill imposes certain new requirements on infant formula manufacturers and the Food and Drug Administration (FDA) following the discovery of contaminated, adulterated, or misbranded infant formula.\u00a0</p><p>Specifically, the bill requires infant formula manufacturers to report to the\u00a0FDA\u00a0within one business day of learning that formula that was\u00a0processed by the manufacturer but that is\u00a0no longer within the manufacturer\u2019s control may not provide required nutrients or may be otherwise adulterated or misbranded.\u00a0</p><p>Further, if any testing of finished infant formula reveals the presence of specified microorganisms (e.g., salmonella), the manufacturer must notify the FDA\u00a0within one business day. (Under current law, manufacturers are only required to report contamination to the FDA\u00a0if the affected formula has left the manufacturer\u2019s control.) The manufacturer must also promptly provide the test results to the FDA and consult with the FDA on proper isolation and disposal of the affected product. The FDA must respond to such a notification and begin discussing proper investigative and corrective action with the manufacturer within one business day.\u00a0</p><p>Within 90 days of a report of adulterated, misbranded, or contaminated infant formula, the FDA must determine whether the manufacturer that reported the problem has performed, or is performing, appropriate investigative and corrective action.\u00a0</p><p>Finally, the FDA is required to periodically report on the infant formula supply chain and efforts to improve the safety and supply of infant formula, and must consult with other federal agencies and infant formula stakeholders on these issues. \u00a0</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s272"
    },
    "title": "Protect Infant Formula from Contamination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Infant Formula from Contamination Act</strong></p><p>This bill imposes certain new requirements on infant formula manufacturers and the Food and Drug Administration (FDA) following the discovery of contaminated, adulterated, or misbranded infant formula.\u00a0</p><p>Specifically, the bill requires infant formula manufacturers to report to the\u00a0FDA\u00a0within one business day of learning that formula that was\u00a0processed by the manufacturer but that is\u00a0no longer within the manufacturer\u2019s control may not provide required nutrients or may be otherwise adulterated or misbranded.\u00a0</p><p>Further, if any testing of finished infant formula reveals the presence of specified microorganisms (e.g., salmonella), the manufacturer must notify the FDA\u00a0within one business day. (Under current law, manufacturers are only required to report contamination to the FDA\u00a0if the affected formula has left the manufacturer\u2019s control.) The manufacturer must also promptly provide the test results to the FDA and consult with the FDA on proper isolation and disposal of the affected product. The FDA must respond to such a notification and begin discussing proper investigative and corrective action with the manufacturer within one business day.\u00a0</p><p>Within 90 days of a report of adulterated, misbranded, or contaminated infant formula, the FDA must determine whether the manufacturer that reported the problem has performed, or is performing, appropriate investigative and corrective action.\u00a0</p><p>Finally, the FDA is required to periodically report on the infant formula supply chain and efforts to improve the safety and supply of infant formula, and must consult with other federal agencies and infant formula stakeholders on these issues. \u00a0</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s272"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s272is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s272rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s272es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protect Infant Formula from Contamination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-02T11:03:24Z"
    },
    {
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "A bill to improve the safety of infant formula through testing of infant formula for microorganisms, and for other purposes.",
      "titleType": "Official Titles as Amended by Senate",
      "titleTypeCode": "8",
      "updateDate": "2026-04-29T10:56:46Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Protect Infant Formula from Contamination Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-29T04:53:33Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Protect Infant Formula from Contamination Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-01-30T04:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Infant Formula from Contamination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the safety of infant formula through testing of infant formula for microorganisms and toxic elements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:20Z"
    }
  ]
}
```
