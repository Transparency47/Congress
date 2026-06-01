# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3756
- Title: Poverty Statistics Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 3756
- Origin chamber: Senate
- Introduced date: 2026-02-02
- Update date: 2026-02-10T00:32:32Z
- Update date including text: 2026-02-10T00:32:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in Senate
- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-02-02: Introduced in Senate

## Actions

- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3756",
    "number": "3756",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Poverty Statistics Enhancement Act",
    "type": "S",
    "updateDate": "2026-02-10T00:32:32Z",
    "updateDateIncludingText": "2026-02-10T00:32:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T22:22:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3756is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3756\nIN THE SENATE OF THE UNITED STATES\nFebruary 2, 2026 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Bureau of the Census, in measuring poverty, to incorporate the distributional analysis of household income used by the Congressional Budget Office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Poverty Statistics Enhancement Act .\n#### 2. Definitions and special rules\nIn this Act:\n**(1) Administering agency**\nThe term administering agency means a Federal, State, or local governmental agency responsible for assessing income, collecting revenue, administering a benefit, or collecting, compiling, and analyzing data related to income assessments, revenue collections, or benefits administration.\n**(2) Director**\nThe term Director means the Director of the Bureau of the Census.\n**(3) Earned income**\n**(A) In general**\nThe term earned income means income paid to individuals from the following:\n**(i)**\nEarnings from employment or self-employment, including employment by a governmental entity to perform specific services, with continued employment conditional on successful delivery of those services.\n**(ii)**\nInterest.\n**(iii)**\nDividends.\n**(iv)**\nRents, royalties, and estates and trusts.\n**(v)**\nRealized capital gains.\n**(vi)**\nThe monetary value of employer-paid benefits, including\u2014\n**(I)**\nhealth insurance premiums;\n**(II)**\nthe actuarial value of\u2014\n**(aa)**\nemployer-funded health insurance net of employee contributions;\n**(bb)**\nlife insurance premiums;\n**(cc)**\ncontributions to a health savings account (as defined in section 223(d) of the Internal Revenue Code of 1986);\n**(dd)**\ncontributions to a qualified cash or deferred arrangement (as defined in section 401(k)(2) of such Code);\n**(ee)**\ncontributions to an individual retirement plan (as defined in section 7701(a)(37) of such Code); and\n**(ff)**\nemployer contributions to a defined contribution retirement plan (as defined in section 414(i) of such Code);\n**(III)**\nbenefits from a defined benefit retirement plan (as defined in section 414(j) of such Code) at the time the benefits are delivered;\n**(IV)**\nbenefits provided to government employees tied specifically to their employment, including veterans benefits; and\n**(V)**\nother benefits paid by an employer during retirement, including pensions, healthcare coverage, and other benefits, counted at the time at which the benefit is received.\n**(vii)**\nIn-kind compensation such as cost-free or reduced-cost lodging or meals, except for items required by the employer for performing work, such as uniforms or personal protective equipment.\n**(B) Special rules for earned income**\n**(i) Adjustments generally**\nFor purposes of subparagraph (A), all types of earned income shall be reconciled and adjusted to known, reliable independent benchmarks, including benchmarks produced by statistical agencies, programmatic agencies, the Internal Revenue Service, private sources, and such other sources as the Director determines appropriate.\n**(ii) Readjustments**\nIn addition to adjusting earned income under clause (i), additional adjustments shall be made for missing and misreported data based on existing and future research by the Bureau of the Census, other government agencies, academic researchers, and other private research.\n**(4) Government transfer payments**\n**(A) In general**\nThe term government transfer payments means any money, goods, services, or discounts provided to individuals, families, or households by or at the direction of Federal Government or State, local, or other government sources, including agencies and agents thereof, or by private entities at the direction of any such source, that are not payments for services performed as an employee or that are not provided equally to all legal residents of the United States without any conditions related to income, assets, economic status, age, social condition, or any other restriction.\n**(B) Inclusions**\nThe term government transfer payments includes the following:\n**(i)**\nUnemployment insurance compensation.\n**(ii)**\nWorkers\u2019 compensation.\n**(iii)**\nBenefits administered by the Social Security Administration, including\u2014\n**(I)**\nold-age insurance benefits and disability insurance benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ); and\n**(II)**\nsupplemental security income benefits under title XVI of such Act ( 42 U.S.C. 1381 et seq. ).\n**(iv)**\nBenefits under the Railroad Retirement Act of 1974 ( 45 U.S.C. 231 et seq. ).\n**(v)**\nOther disability benefits from government, except those provided to government employees as part of their employment compensation.\n**(vi)**\nBenefits provided under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), including any income-related subsidy described in section 1860D\u201314 of such Act ( 42 U.S.C. 1395w\u2013114 ), and any other reduction in premiums or cost sharing, such as deductibles, copayments, or coinsurance under such title.\n**(vii)**\nSo much of the amount of any income tax refund paid to a taxpayer which is attributable to\u2014\n**(I)**\nthe earned income credit under section 32 of the Internal Revenue Code of 1986;\n**(II)**\nthe child tax credit under section 24 of such Code; and\n**(III)**\nany other refundable credit under subpart C of part IV of subchapter A of chapter 1 of such Code.\n**(viii)**\nAssistance or benefits provided under the Temporary Assistance for Needy Families program established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ).\n**(ix)**\nMedical assistance provided under the Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).\n**(x)**\nChild health assistance or pregnancy-related assistance provided under the State Children's Health Insurance Program established under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. ).\n**(xi)**\nBenefits provided pursuant to an Indian health program (as defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )).\n**(xii)**\nPremium tax credits under section 36B of the Internal Revenue Code of 1986, cost-sharing reduction payments under section 1402 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18071 ), or any other payment that reduces the premium amount paid by the enrollee.\n**(xiii)**\nAny other government payments to assist in purchasing medical care or health insurance.\n**(xiv)**\nBenefits under the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ).\n**(xv)**\nFree and reduced price meals provided under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) and section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ).\n**(xvi)**\nBenefits and services provided under the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ).\n**(xvii)**\nMeals provided under the child and adult care food program established under section 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ).\n**(xviii)**\nRental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), including housing choice vouchers and project-based rental assistance.\n**(xix)**\nAssistance provided by the Rural Housing Service of the Department of Agriculture, including rental assistance.\n**(xx)**\nAssistance (including services) under the Low-Income Home Energy Assistance Program, established under the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621 et seq. ).\n**(xxi)**\nA Federal Pell Grant under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ).\n**(xxii)**\nSo much of the American Opportunity Tax Credit under section 25A of the Internal Revenue Code of 1986 as is allowed under subsection (i) thereof.\n**(xxiii)**\nSuch other transfers by or at the direction of Federal Government or State, local, or other government sources that the Director determines to be consistent with subparagraph (A) using available data sources.\n**(5) Income tax data**\nThe term income tax data means return information, as defined in section 6103(b)(2) of the Internal Revenue Code of 1986 ( 26 U.S.C. 6103(b)(2) ).\n**(6) Statistical agency**\nThe term statisical agency means\u2014\n**(A)**\nthe Bureau of Labor Statistics of the Department of Labor;\n**(B)**\nthe Bureau of Economic Analysis of the Department of Commerce; and\n**(C)**\nany other Federal, State, or local government entity that collects, processes, or publishes data related to any of the components of income covered by this Act.\n**(7) Taxes**\n**(A) In general**\n**(i) General definition**\nThe term taxes means all money revenues paid by individuals, families, or households to the Federal Government or a State, local, or other government either directly or indirectly through an employer or other entity based on their earnings from employment, savings, investing, real estate, trusts, or other sources or on the value, ownership, or usage of real estate property, personal property, other assets of any kind, or purchases of goods and services (including both real and financial).\n**(ii) Inclusions**\nThe term taxes includes\u2014\n**(I)**\nemployment taxes under subtitle C of the Internal Revenue Code of 1986 (whether paid by the employer or employee);\n**(II)**\nincome taxes, including taxes on investment income;\n**(III)**\ncorporate income taxes allocated to shareholders based on best research on share of corporate taxes that reduce dividends;\n**(IV)**\ncorporate income taxes allocated to employees based on best research on share of corporate taxes that reduce compensation;\n**(V)**\nself-employment income and payroll taxes;\n**(VI)**\nproperty taxes;\n**(VII)**\ncapital gains taxes;\n**(VIII)**\nestate taxes;\n**(IX)**\ninheritance taxes;\n**(X)**\ngift taxes;\n**(XI)**\nsales taxes, use taxes, value added taxes, or any other fee collected by government on sales of any goods or any services (either real or financial) to households or individuals;\n**(XII)**\nexcise taxes paid either separately or included as part of the price paid for a good or service;\n**(XIII)**\ntariffs and duties paid either directly or as part of the price paid for a good or service; and\n**(XIV)**\nsuch other sources of money revenues that the Director determines to be consistent with clause (i).\n**(B) Special rules for determining amounts of tax**\n**(i) In general**\nFor purposes of subparagraph (A), totals of taxes shall be reconciled and adjusted to sum to total tax and other revenue income available from other reliable sources, including the Office of Management and Budget, the Department of the Treasury, and the Bureau of Economic Analysis.\n**(ii) Treatment of tax credits**\nWith respect to any taxpayer:\n**(I)**\nThe amount of taxes paid shall be determined without regard to any refund paid to the taxpayer which is attributable to any refundable credit under subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986.\n**(II)**\nThe amount of any refund paid to the taxpayer which is attributable to any such refundable credit shall be treated as a government transfer payment in accordance with paragraph (3).\n#### 3. Adjustment of Census income inequality calculation\n##### (a) New methodology\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Director, in consultation with the heads of other appropriate Federal, State, and local agencies, as determined by the Director, shall implement a new methodology to measure poverty, in addition to the Official Poverty Measure and the Supplemental Poverty Measure, that\u2014\n**(A)**\nuses the methodology outlined in the report of the Congressional Budget Office titled Reconciling the Official Poverty Measure and CBO\u2019s Distributional Analysis of Household Income ; and\n**(B)**\nmeasures the income of an individual as the amount equal to\u2014\n**(i)**\nthe sum of earned income and government transfer payments received by the individual, less\n**(ii)**\nthe taxes paid by the individual.\n**(2) Resolution of potential conflict**\nTo the extent of any conflict between the requirements under subparagraphs (A) and (B) of paragraph (1), the requirement under such subparagraph (A) shall supersede the requirement under such subparagraph (B).\n##### (b) Agency data\n**(1) Federal agencies**\nNot later than 180 days after the head of a Federal agency receives a request from the Director for data possessed or reasonably obtainable by such Federal agency for carrying out this section, such head shall make available to the Director such data to the extent otherwise permitted by law.\n**(2) State and local agencies**\nThe Director may request the head of a State or local agency that is an administering agency to provide such data as the Director determines necessary to carry out this section.\n##### (c) Publication of data\n**(1) Data report**\nNot later than 1 year after the date on which the Director implements the new methodology required under subsection (a), the Director shall submit to Congress a report detailing the implementation of this Act, including the availability and quality of data from the administering agencies from which the Director has requested information for carrying out this section.\n**(2) Measurement report**\n**(A) In general**\nNot later than 1 year after the date on which the Director implements the new methodology required under subsection (a), the Director shall submit to Congress a report detailing the implementation of this Act, including\u2014\n**(i)**\nthe recalculated measures of income inequality based on the new calculation methodology implemented under subsection (a);\n**(ii)**\na comparison between the recalculated measures of income inequality and of household income dispersion based on the new calculation methodology implemented under subsection (a) and such measures based on the calculation methodologies in use for such measures on the day before the date on which such new calculation methodology was implemented; and\n**(iii)**\na comparison between each statistic tracked by the Bureau of the Census based on the new calculation methodology implemented under subsection (a) and such statistic based on the calculation methodologies in use for such statistic on the day before the date on which such new calculation methodology was implemented.\n**(B) Data sources**\n**(i) In general**\nThe Director shall use the best available data sources in creating the report required under subparagraph (A), including the use of surveys previously collected by the Bureau of the Census, data from other statistical agencies, data from private sources, and, in cases of missing or unknown data, statistical imputations.\n**(ii) Survey augmentation**\nIn carrying out clause (i), the Director may augment surveys being carried out by the Bureau of the Census or the Bureau of Labor Statistics of the Department of Labor.\n**(3) Statistics publication**\nFor all publications and data sets issued after the date on which the Director implements the new methodology required under subsection (a), the Director shall use such new calculation methodology to calculate each instance of each measure or statistic based on such methodology, including each historical instance.\n##### (d) Protection and disclosure of personally identifiable information\n**(1) In general**\nThe security, disclosure, and confidentiality provisions set for in sections 9 and 23 of title 13, United States Code, shall apply to personally identifiable information obtained by the Bureau of the Census pursuant to this Act.\n**(2) Restricted access to personally identifiable information**\nAccess to personally identifiable information collected to supplement the restricted-use Current Population Survey Annual Social and Economic Supplements in accordance with subsection (b)(1) shall be available only to those who have access to the Current Population Survey data with the permission of the Bureau of the Census and in accordance with any other applicable provision of Federal and State law.\n**(3) Criminal penalties**\nAny individual who knowingly accesses or discloses personally identifiable information in violation of this section shall be fined not more than $300,000, imprisoned for not more than 5 years, or both.",
      "versionDate": "2026-02-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-10T00:32:32Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3756is.xml"
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
      "title": "Poverty Statistics Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Poverty Statistics Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Bureau of the Census, in measuring poverty, to incorporate the distributional analysis of household income used by the Congressional Budget Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:38Z"
    }
  ]
}
```
